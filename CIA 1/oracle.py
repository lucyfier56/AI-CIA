# oracle.py

def oracle(possible_solutions, goal):
    return goal if goal in possible_solutions else None

# Example usage
solutions = ['A', 'B', 'C', 'goal', 'D']
goal = 'goal'
result = oracle(solutions, goal)
print(f"Oracle found: {result}")
