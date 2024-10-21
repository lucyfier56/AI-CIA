

def british_museum_search(possible_solutions, goal):
    for solution in possible_solutions:
        if solution == goal:
            return solution
    return None


solutions = ['solution1', 'solution2', 'goal', 'solution3']
goal = 'goal'
result = british_museum_search(solutions, goal)
print(f"Goal found: {result}")
