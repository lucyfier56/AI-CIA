import math

def alpha_beta(node, depth, alpha, beta, is_maximizing):
    # Base case: evaluate the heuristic value of the node
    if depth == 0 or is_terminal(node):
        return evaluate(node)

    if is_maximizing:
        max_eval = -math.inf
        for child in get_children(node):
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = math.inf
        for child in get_children(node):
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
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
        {'is_terminal': True, 'value': 3, 'children': []},
        {'is_terminal': True, 'value': 5, 'children': []},
        {'is_terminal': True, 'value': 2, 'children': []},
        {'is_terminal': True, 'value': 9, 'children': []},
        {'is_terminal': True, 'value': 0, 'children': []}
    ]
}

result = alpha_beta(root, depth=3, alpha=-math.inf, beta=math.inf, is_maximizing=True)
print(f"Alpha-Beta result: {result}")
