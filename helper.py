from scipy.optimize import linprog


def allocate_demand(instance, demands):
    # Auxiliary
    products = list(range(instance['products']))
    plants = list(range(instance['plants']))

    # Objective function coefficients
    c = [-1.0 for product in products for plant in plants]

    # Capacity constraints
    b_ub = []
    A_ub = []
    for plant in plants:
        b_ub.append(instance['capacities'][plant])
        A_ub.append([1.0 if j == plant else 0 for i in products for j in plants])

    # Demand constraints
    for product in products:
        b_ub.append(demands[product])
        A_ub.append([1.0 if i == product else 0.0 for i in products for j in plants])

    # Configuration constraints
    bounds = []
    for i in products:
        for j in plants:
            bounds.append((0.0, 0.0) if instance['configuration'][i][j] < 1 else (0.0, None))

    res = linprog(c, A_ub, b_ub, bounds=bounds)

    number_sales = sum(res.x)
    utilization = number_sales / sum(instance['capacities'])
    return number_sales, utilization, res.x


def simulate(instance, sample_demand, number_times):
    observations = []
    for _ in range(number_times):
        demands = sample_demand(instance)
        number_sales, utilization, allocation = allocate_demand(instance, demands)
        observations.append([number_sales, utilization])
    return observations

