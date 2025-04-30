# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        node_to_delete, source = self.find_node(root, key)
        if not node_to_delete:
            return root
        new = node_to_delete.right
        if new: 
            if not new.left:
                new.left = node_to_delete.left
            else:
                left = new.left
                while left.left:
                    left = left.left
                left.left = node_to_delete.left
        else:
            new = node_to_delete.left
        if source:
            if source.left == node_to_delete:
                source.left = new
            else:
                source.right = new
            return root
        else:
            return new

    def find_node(self, root, key, source=None) -> TreeNode:
        if root == None:
            return None, None
        if key > root.val:
            return self.find_node(root.right, key, root)
        if key < root.val:
            return self.find_node(root.left, key, root)
        return root, source
