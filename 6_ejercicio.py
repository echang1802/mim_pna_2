from helper import simulate
import numpy as np

np.random.seed(42)

flexibilidad_plena = {
    'products': 6,  # RELLENAR
    'plants': 4,  # RELLENAR
    'capacities': [1000, 1500, 2000, 1800],  # RELLENAR,
    'demands' : [500, 1000, 800, 1500, 600, 1900],
    'configuration': [
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]
    ]  # RELLENAR
}

custom = {
    'products': 6,  # RELLENAR
    'plants': 4,  # RELLENAR
    'capacities': [1000, 1500, 2000, 1800],  # RELLENAR
                # [1100, 1800, 2500, 2500]
    'demands' : [500, 1000, 800, 1500, 600, 1900],
    'configuration': [
         [1,0,0,0],
         [0,1,0,0],
         [0,0,1,0],
         [0,0,0,1],
         [1,1,1,0],
         [0,1,1,1]
    ]  # RELLENAR
}

def poisson_demand_sampler(instance):
    # Tiene que devolver una lista con la demanda para cada producto.
    return [np.random.poisson(demand) for demand in instance["demands"]]  # RELLENAR. Pista: np.random.poisson


# Devuelve observaciones de la forma [[ventas_1, utilizacion_1], ..., [ventas_N, utilizacion_N]]
observations = simulate(flexibilidad_plena, poisson_demand_sampler, 10000)

# zip(*[[1, 2], [3, 4]]) = [1, 3], [2, 4]
sales, utilizaciones = zip(*observations)
es_6300 = [observation > 6299 for observation in sales]

print('Flexibilidad plena')
print('Ventas: %.2f' % (sum(sales) / len(sales)))
print('Ventas: %.2f' % np.std(sales))
print('Utilizacion: %.2f' % (sum(utilizaciones) / len(utilizaciones)))
print('P(Ventas=6300): %.2f' % (sum(es_6300) / len(es_6300)))

# Devuelve observaciones de la forma [[ventas_1, utilizacion_1], ..., [ventas_N, utilizacion_N]]
observations = simulate(custom, poisson_demand_sampler, 10000)

# zip(*[[1, 2], [3, 4]]) = [1, 3], [2, 4]
sales, utilizaciones = zip(*observations)
es_6300 = [observation > 6299 for observation in sales]

print('')
print('Custom')
print('Ventas: %.2f' % (sum(sales) / len(sales)))
print('Ventas: %.2f' % np.std(sales))
print('Utilizacion: %.2f' % (sum(utilizaciones) / len(utilizaciones)))
print('P(Ventas=6300): %.2f' % (sum(es_6300) / len(es_6300)))
