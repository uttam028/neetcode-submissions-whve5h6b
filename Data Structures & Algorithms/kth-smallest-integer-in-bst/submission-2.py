# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = k
        find = None
        def traverse(node: TreeNode):
            nonlocal visited, find
            if(node.left is not None):
                traverse(node.left)
            visited -= 1
            if(visited==0):
                find = node.val
                return
            if(node.right is not None):
                traverse(node.right)
        traverse(root)
        return find
