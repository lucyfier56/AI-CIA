# hill_climbing.py

def hill_climbing(problem, start):
    current = start
    while True:
        neighbors = problem.get_neighbors(current)
        next_move = max(neighbors, key=problem.fitness)
        if problem.fitness(next_move) <= problem.fitness(current):
            return current
        current = next_move

# Example usage
class Problem:
    def get_neighbors(self, node):
        return [node - 1, node + 1]
    
    def fitness(self, node):
        return -abs(node - 10)

problem = Problem()
start = 0
result = hill_climbing(problem, start)
print(f"Optimal solution: {result}")
