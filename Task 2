import random

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def path_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    cost += graph[path[-1]][path[0]]  
    return cost


def get_neighbor(path):
    neighbor = path[:]
    i, j = random.sample(range(len(path)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor


def hill_climbing():
    current = list(range(len(graph)))
    random.shuffle(current)

    current_cost = path_cost(current)

    while True:
        neighbor = get_neighbor(current)
        neighbor_cost = path_cost(neighbor)

        if neighbor_cost < current_cost:
            current = neighbor
            current_cost = neighbor_cost
        else:
            break


output
Best Path: [1, 0, 3, 2, 1]
Minimum Cost: 95
