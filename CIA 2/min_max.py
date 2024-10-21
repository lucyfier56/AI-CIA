import math

def min_max(node, depth, is_maximizing):
    # Base case: evaluate the heuristic value of the node
    if depth == 0 or is_terminal(node):
        return evaluate(node)

    if is_maximizing:
        max_eval = -math.inf
        for child in get_children(node):
            eval = min_max(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for child in get_children(node):
            eval = min_max(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def is_terminal(node):
    # Check if the node is a terminal node
    return node['is_terminal']

def evaluate(node):
    # Heuristic evaluation of the node
    return node['value']

def get_children(node):
    # Get child nodes from the current node
    return node['children']

# Example usage
root = {
    'is_terminal': False,
    'value': 0,
    'children': [
        {'is_terminal': True, 'value': 1},
        {'is_terminal': True, 'value': -1},
        {'is_terminal': True, 'value': 0}
    ]
}

result = min_max(root, depth=1, is_maximizing=True)
print(f"Min-Max result: {result}")
