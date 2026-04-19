# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, node:Optional[TreeNode]):
        if(node is None):
            return
        self.traverse(node.left)
        self.traverse(node.right)        
        left = node.left
        right = node.right
        node.left = right
        node.right = left

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root is None):
            return None
        self.traverse(root)
        return root