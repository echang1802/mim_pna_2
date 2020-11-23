from helper import simulate
import numpy as np

np.random.seed(42)

flexibilidad_plena = {
    'products': 0,  # RELLENAR
    'plants': 0,  # RELLENAR
    'capacities': [],  # RELLENAR
    'configuration': []  # RELLENAR
}

custom = {
    'products': 0,  # RELLENAR
    'plants': 0,  # RELLENAR
    'capacities': [],  # RELLENAR
    'configuration': []  # RELLENAR
}

def poisson_demand_sampler(instance):
    # Tiene que devolver una lista con la demanda para cada producto.
    return []  # RELLENAR. Pista: np.random.poisson


# Devuelve observaciones de la forma [[ventas_1, utilizacion_1], ..., [ventas_N, utilizacion_N]]
observations = simulate(flexibilidad_plena, poisson_demand_sampler, 10000)

# zip(*[[1, 2], [3, 4]]) = [1, 3], [2, 4]
sales, utilizaciones = zip(*observations)
es_6300 = [observation > 6299 for observation in sales]

print('Flexibilidad plena')
print('Ventas: %.2f' % (sum(sales) / len(sales)))
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
print('Utilizacion: %.2f' % (sum(utilizaciones) / len(utilizaciones)))
print('P(Ventas=6300): %.2f' % (sum(es_6300) / len(es_6300)))
