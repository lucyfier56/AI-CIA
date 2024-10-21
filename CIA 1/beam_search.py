# beam_search.py

def beam_search(problem, start, beam_width):
    current = [start]
    while True:
        candidates = []
        for state in current:
            candidates.extend(problem.get_neighbors(state))
        current = sorted(candidates, key=problem.fitness)[:beam_width]
        if all(problem.fitness(state) == problem.optimal for state in current):
            return current

# Example usage
class Problem:
    optimal = 10
    def get_neighbors(self, node):
        return [node - 1, node + 1]
    
    def fitness(self, node):
        return -abs(node - self.optimal)

problem = Problem()
start = 0
beam_width = 2
result = beam_search(problem, start, beam_width)
print(f"Optimal solution: {result}")
