class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        comp = 0

        def dfs(node):
            for i in adj[node]:
                if i not in visit:
                    visit.add(i)
                    dfs(i)


        for i in range(n):
            if i not in visit:
                comp += 1
                visit.add(i)
                dfs(i)

        return comp