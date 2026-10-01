
colors = ["Red", "Green", "Blue", "Yellow"]

zones = ["A", "B", "C", "D", "E"]
neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E"],
    "E": ["C", "D"]
}
def is_valid(zone, color, assignment):

    for neighbor in neighbors[zone]:

        if neighbor in assignment:
            if assignment[neighbor] == color:
                return False

    return True
def backtracking(assignment):
    if len(assignment) == len(zones):
        return assignment
    for zone in zones:
        if zone not in assignment:
            break
    for color in colors:
        if is_valid(zone, color, assignment):

            assignment[zone] = color
            result = backtracking(assignment)

            if result is not None:
                return result

            del assignment[zone]

    return None
solution = backtracking({})

if solution:
    print("Valid Campus Map Coloring:")
    
    for zone in zones:
        print(zone, "->", solution[zone])

else:
    print("No valid coloring found.")


Input/Output
Valid Campus Map Coloring:
A -> Red
B -> Green
C -> Blue
D -> Red
E -> Green
