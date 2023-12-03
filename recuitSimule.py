import random
import math

def knapsack_simulated_annealing(items, max_weight, temperature_initiale, taux_refroidissement, nombre_iterations):
    solution_actuelle = []
    meilleure_solution = []
    poids_actuel = 0
    meilleure_valeur = 0

    # Solution initiale
    for item in items:
        if random.random() < 0.5:
            solution_actuelle.append(item['id'])
            poids_actuel += item['weight']

    # Définir la température initiale
    temperature = temperature_initiale

    for i in range(nombre_iterations):
        # Générer une solution voisine
        solution_voisine = solution_actuelle.copy()
        item_aleatoire = random.choice(items)
        if item_aleatoire['id'] in solution_voisine:
            solution_voisine.remove(item_aleatoire['id'])
            poids_actuel -= item_aleatoire['weight']
        else:
            solution_voisine.append(item_aleatoire['id'])
            poids_actuel += item_aleatoire['weight']

        # Calculer la valeur de la solution voisine
        valeur_voisine = sum(item['value'] for item in items if item['id'] in solution_voisine)

        # Calculer la probabilité d'acceptation
        probabilite_acceptation = math.exp((valeur_voisine - meilleure_valeur) / temperature)

        # Accepter ou rejeter la solution voisine
        if valeur_voisine > meilleure_valeur or random.random() < probabilite_acceptation:
            solution_actuelle = solution_voisine.copy()
            meilleure_valeur = valeur_voisine

        # Mettre à jour la meilleure solution si nécessaire
        if meilleure_valeur > sum(item['value'] for item in items if item['id'] in meilleure_solution):
            meilleure_solution = solution_actuelle.copy()

        # Refroidir la température
        temperature *= taux_refroidissement

    return meilleure_solution

# Définir les articles
items = [
    {'name': 'chaise', 'value': 10, 'id': 1, 'weight': 50},
    {'name': 'table', 'value': 20, 'id': 2, 'weight': 30},
    {'name': 'lampe', 'value': 15, 'id': 3, 'weight': 40},
]

poids_max = 80
temperature_initiale = 100
taux_refroidissement = 0.95
nombre_iterations = 1000

meilleure_solution = knapsack_simulated_annealing(items, poids_max, temperature_initiale, taux_refroidissement, nombre_iterations)
print("Meilleure solution :", meilleure_solution)
