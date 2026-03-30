"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {} # Map nodes on the original graph to the new copy graph

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for nb in node.neighbors:
                copy.neighbors.append(dfs(nb))

            return copy

        if node is not None:
            return dfs(node)
    