# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.depth = 0
    def traverse(self, node: TreeNode, max: int):
        if(node.left is not None):
            self.traverse(node.left, max+1)
        if(node.right is not None):
            self.traverse(node.right, max+1)
        if(max> self.depth):
            self.depth = max
        return
        

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root is not None):
            self.traverse(root, 1)
            return self.depth
        return 0
