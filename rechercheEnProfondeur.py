items = [
    {'name': 'chaise', 'value': 10, 'id': 1, 'weight': 50},
    {'name': 'table', 'value': 20, 'id': 2, 'weight': 30},
    {'name': 'lampe', 'value': 15, 'id': 3, 'weight': 40},
]

def knapsack_dfs(items, capacite):
    def dfs(index, poids_actuel, valeur_actuelle, articles_selectionnes):
        if index >= len(items) or poids_actuel >= capacite:
            return valeur_actuelle, articles_selectionnes

        # Essayer d'inclure l'article actuel
        valeur_incluse, articles_inclus = dfs(index + 1, poids_actuel + items[index]['weight'], valeur_actuelle + items[index]['value'], articles_selectionnes + [items[index]])

        # Essayer d'exclure l'article actuel
        valeur_exclue, articles_exclus = dfs(index + 1, poids_actuel, valeur_actuelle, articles_selectionnes)

        # Retourner la valeur maximale et les articles correspondants
        if valeur_incluse > valeur_exclue:
            return valeur_incluse, articles_inclus
        else:
            return valeur_exclue, articles_exclus

    # Démarrer la recherche en profondeur
    valeur_max, articles_selectionnes = dfs(0, 0, 0, [])

    return valeur_max, articles_selectionnes

# Exemple d'utilisation
capacite = 70
valeur_max, articles_selectionnes = knapsack_dfs(items, capacite)
print("Valeur maximale :", valeur_max)
print("Articles sélectionnés :", articles_selectionnes)
