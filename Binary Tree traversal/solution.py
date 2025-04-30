# Pre-order traversal
def pre_order(node):
    return [node.data] + pre_order(node.left) + pre_order(node.right) if node else []

# In-order traversal
def in_order(node):
    return in_order(node.left) + [node.data] + in_order(node.right) if node else []

# Post-order traversal
def post_order(node):
    return post_order(node.left) + post_order(node.right) + [node.data] if node else []
