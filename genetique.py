import random

def genetic_bag_algorithm(items, max_weight, population_size, generations):
    # Initialiser la population
    population = []
    for _ in range(population_size):
        chromosome = [random.randint(0, 1) for _ in range(len(items))]
        population.append(chromosome)

    # Boucle d'évolution
    for _ in range(generations):
        # Évaluer la fitness de chaque chromosome
        fitness_scores = []
        for chromosome in population:
            total_weight = sum(chromosome[i] * items[i]['weight'] for i in range(len(items)))
            total_value = sum(chromosome[i] * items[i]['value'] for i in range(len(items)))
            if total_weight <= max_weight:
                fitness_scores.append(total_value)
            else:
                fitness_scores.append(0)

        # Sélectionner les parents pour la reproduction
        parents = []
        for _ in range(population_size // 2):
            parent1 = random.choices(population, weights=fitness_scores)[0]
            parent2 = random.choices(population, weights=fitness_scores)[0]
            parents.append((parent1, parent2))

        # Créer une nouvelle génération par crossover et mutation
        population = []
        for parent1, parent2 in parents:
            child1 = parent1[:len(parent1) // 2] + parent2[len(parent2) // 2:]
            child2 = parent2[:len(parent2) // 2] + parent1[len(parent1) // 2:]
            population.append(child1)
            population.append(child2)

        # Effectuer la mutation
        for i in range(len(population)):
            if random.random() < 0.1:  # Taux de mutation de 10%
                gene_index = random.randint(0, len(items) - 1)
                population[i][gene_index] = 1 - population[i][gene_index]

    # Trouver la meilleure solution
    best_solution = None
    best_fitness = 0
    for chromosome in population:
        total_weight = sum(chromosome[i] * items[i]['weight'] for i in range(len(items)))
        total_value = sum(chromosome[i] * items[i]['value'] for i in range(len(items)))
        if total_weight <= max_weight and total_value > best_fitness:
            best_solution = chromosome
            best_fitness = total_value

    return best_solution

# Définir les articles
items = [
    {'name': 'chaise', 'value': 10, 'id': 1, 'weight': 50},
    {'name': 'table', 'value': 20, 'id': 2, 'weight': 30},
    {'name': 'lampe', 'value': 15, 'id': 3, 'weight': 40},
   
]

# Définir le poids maximum et autres paramètres
max_weight = 80
population_size = 100
generations = 100

# Exécuter l'algorithme génétique du sac à dos
best_solution = genetic_bag_algorithm(items, max_weight, population_size, generations)

# Afficher la meilleure solution
print("Meilleure solution :")
for i in range(len(items)):
    if best_solution[i] == 1:
        print(items[i]['name'])
