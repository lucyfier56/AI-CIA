# branch_and_bound.py

def branch_and_bound(problem, start):
    best_solution = start
    best_cost = problem.cost(start)
    
    def b_and_b(node):
        nonlocal best_solution, best_cost
        if problem.cost(node) < best_cost:
            best_solution = node
            best_cost = problem.cost(node)
        for child in problem.get_children(node):
            if problem.bound(child) < best_cost:
                b_and_b(child)

    b_and_b(start)
    return best_solution

# Example usage
class Problem:
    def get_children(self, node):
        return [node - 1, node + 1]
    
    def cost(self, node):
        return abs(node - 10)
    
    def bound(self, node):
        return abs(node - 10)

problem = Problem()
start = 0
result = branch_and_bound(problem, start)
print(f"Best solution: {result}")
