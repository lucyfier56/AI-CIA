# bfs.py

from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == goal:
            return True
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
    return False

# Example usage
graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
start = 'A'
goal = 'E'
result = bfs(graph, start, goal)
print(f"Goal found: {result}")
