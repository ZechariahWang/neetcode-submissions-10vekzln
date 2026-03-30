# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxVal=float('-inf')
        def dfs(node,maxVal):
            count=0

            if not node:
                return 0

            if node.val>=maxVal:
                count=1
            else:
                count=0
            
            maxVal=max(node.val,maxVal)
            
            left=dfs(node.left,maxVal)
            right=dfs(node.right,maxVal)
            return count+left+right
        
        return dfs(root,maxVal)

        