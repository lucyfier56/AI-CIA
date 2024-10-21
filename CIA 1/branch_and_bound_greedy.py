import heapq

def branch_and_bound_greedy(graph, start, goal):
    frontier = [(0, start, [])]  # (cost, current node, path)
    visited = set()

    while frontier:
        (cost_so_far, current, path) = heapq.heappop(frontier)

        if current in visited:
            continue

        path = path + [current]

        if current == goal:
            return path, cost_so_far
        
        visited.add(current)

        for next_node, weight in graph.get(current, []):
            heapq.heappush(frontier, (cost_so_far + weight, next_node, path))
    
    return None

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

result = branch_and_bound_greedy(graph, 'A', 'D')
print(f"Branch and Bound Greedy result: {result}")
