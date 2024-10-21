import heapq

def branch_and_bound_greedy_exit(graph, start, goal, exit_condition):
    frontier = [(0, start, [])]  # (cost, current node, path)
    visited = set()

    while frontier:
        (cost_so_far, current, path) = heapq.heappop(frontier)

        if exit_condition(cost_so_far):
            print(f"Exiting: Cost exceeded threshold with cost {cost_so_far}.")
            break
        
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
def exit_condition(cost):
    return cost > 5

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

result = branch_and_bound_greedy_exit(graph, 'A', 'D', exit_condition)
print(f"Branch and Bound Greedy Exit result: {result}")
