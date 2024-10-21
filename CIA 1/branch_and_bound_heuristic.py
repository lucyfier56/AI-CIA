import heapq

def branch_and_bound_heuristic(graph, start, goal, heuristic):
    frontier = [(0, start, [])]  # (heuristic cost, current node, path)
    visited = set()

    while frontier:
        (heuristic_cost, current, path) = heapq.heappop(frontier)

        if current in visited:
            continue

        path = path + [current]

        if current == goal:
            return path, heuristic_cost
        
        visited.add(current)

        for next_node, weight in graph.get(current, []):
            total_cost = heuristic_cost + heuristic(next_node)
            heapq.heappush(frontier, (total_cost, next_node, path))
    
    return None

# Define a simple heuristic function
def heuristic(node):
    # In this example, we use a constant value for demonstration.
    # Replace this with a more meaningful heuristic for your specific problem.
    return 1

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []  # Goal node
}

# Example usage
result = branch_and_bound_heuristic(graph, 'A', 'D', heuristic)
print(f"Branch and Bound Heuristic result: {result}")
