# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def successor(root):
            root = root.right
            while root.left is not None:
                root = root.left
            return root.val
        def predecessor(root):
            root = root.left
            while root.right is not None:
                root = root.right
            return root.val
        if root is None:
            return None
        # search for the node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # leaft node deletion 
            if root.left is None and root.right is None:
                root = None
            # non leaf node deletion
            elif root.right is not None:
                root.val = successor(root)
                root.right = self.deleteNode(root.right,root.val)
            else:
                root.val = predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root