import heapq

def branch_and_bound_greedy_heuristic(graph, start, goal, heuristic):
    frontier = [(0, start, [])]  # (cost + heuristic, current node, path)
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
            total_cost = cost_so_far + weight + heuristic(next_node)
            heapq.heappush(frontier, (total_cost, next_node, path))
    
    return None

# Example usage
def heuristic(node):
    return 1  # Simple heuristic

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

result = branch_and_bound_greedy_heuristic(graph, 'A', 'D', heuristic)
print(f"Branch and Bound Greedy and Heuristic result: {result}")
