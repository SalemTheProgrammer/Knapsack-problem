def knapsack_greedy(items, max_weight):
    # Trier les articles par rapport au ratio valeur/poids de manière décroissante
    sorted_items = sorted(items, key=lambda x: x['value'] / x['weight'], reverse=True)

    total_value = 0
    total_weight = 0
    selected_items = []

    for item in sorted_items:
        # Vérifier si l'ajout de l'article respecte la contrainte de poids
        if total_weight + item['weight'] <= max_weight:
            selected_items.append(item)
            total_value += item['value']
            total_weight += item['weight']

    return selected_items, total_value

# Définir les articles
items = [
    {'name': 'chaise', 'value': 10, 'id': 1, 'weight': 50},
    {'name': 'table', 'value': 20, 'id': 2, 'weight': 30},
    {'name': 'lampe', 'value': 15, 'id': 3, 'weight': 40},
]

max_weight = 70

# Appliquer l'algorithme du sac à dos glouton
selected_items, total_value = knapsack_greedy(items, max_weight)

# Afficher les articles sélectionnés
print("Articles sélectionnés :")
for item in selected_items:
    print(item['name'])
print("Valeur totale :", total_value)
