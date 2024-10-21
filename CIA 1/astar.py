# astar.py

from heapq import heappop, heappush

def astar(problem, start):
    open_list = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: problem.heuristic(start)}
    
    while open_list:
        _, current = heappop(open_list)
        if problem.is_goal(current):
            return reconstruct_path(came_from, current)
        for neighbor in problem.get_neighbors(current):
            tentative_g = g_score[current] + problem.cost(current, neighbor)
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = g_score[neighbor] + problem.heuristic(neighbor)
                heappush(open_list, (f_score[neighbor], neighbor))

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

# Example usage
class Problem:
    def get_neighbors(self, node):
        return [node - 1, node + 1]
    
    def cost(self, current, neighbor):
        return abs(current - neighbor)
    
    def heuristic(self, node):
        return abs(node - 10)
    
    def is_goal(self, node):
        return node == 10

problem = Problem()
start = 0
result = astar(problem, start)
print(f"Path to goal: {result}")
