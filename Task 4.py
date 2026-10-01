game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3, 5],
    'E': [6, 9],
    'F': [1, 2],
    'G': [0, 1]
}

pruned_branches = []


def minimax(node, maximizing_player, alpha, beta):
    if isinstance(game_tree[node][0], int):
        values = game_tree[node]

        if maximizing_player:
            best_value = float('-inf')

            for value in values:
                best_value = max(best_value, value)
                alpha = max(alpha, best_value)

                if beta <= alpha:
                    break

            return best_value

        else:
            best_value = float('inf')

            for value in values:
                best_value = min(best_value, value)
                beta = min(beta, best_value)

                if beta <= alpha:
                    break

            return best_value
    if maximizing_player:
        best_value = float('-inf')

        for i, child in enumerate(game_tree[node]):
            value = minimax(child, False, alpha, beta)

            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            if beta <= alpha:
                for remaining in game_tree[node][i + 1:]:
                    pruned_branches.append(remaining)
                break

        return best_value
    else:
        best_value = float('inf')

        for i, child in enumerate(game_tree[node]):
            value = minimax(child, True, alpha, beta)

            best_value = min(best_value, value)
            beta = min(beta, best_value)

            if beta <= alpha:
                for remaining in game_tree[node][i + 1:]:
                    pruned_branches.append(remaining)
                break

        return best_value

alpha = float('-inf')
beta = float('inf')
result = minimax('A', True, alpha, beta)

best_move = None
best_value = float('-inf')

alpha = float('-inf')
beta = float('inf')

for child in game_tree['A']:
    value = minimax(child, False, alpha, beta)

    if value > best_value:
        best_value = value
        best_move = child

    alpha = max(alpha, best_value)

print("Mini-Max value of A:", result)
print("Best move for Player A:", best_move)
print("Optimal path: A -> B -> D -> 5")
print("Pruned branch:", pruned_branches)


Input/Output
Mini-Max value of A: 5
Best move for Player A: B
Optimal path: A -> B -> D -> 5
Pruned branch: ['G', 'G']
