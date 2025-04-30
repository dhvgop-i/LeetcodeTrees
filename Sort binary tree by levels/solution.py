def tree_by_levels(node):
    if node:
        res = [node.value]
    else:
        return []
    curr = [node]
    while True:
        curr =[[x.left, x.right] for x in curr]
        curr = sum(curr, [])
        if not any(curr):
            return res
        curr = [x for x in curr if x]
        res.extend([x.value for x in curr])