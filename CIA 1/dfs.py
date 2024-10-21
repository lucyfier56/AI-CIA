# dfs.py

def dfs(graph, start, goal, visited=set()):
    if start == goal:
        return True
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True
    return False

# Example usage
graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
start = 'A'
goal = 'E'
result = dfs(graph, start, goal)
print(f"Goal found: {result}")
