class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            graph[u] += [v]
            graph[v] += [u]
        visited = set()
        # print(graph)
        def dfs(node):
            if(node in visited):
                return
            neighbors = graph[node]
            # print('neighbors', neighbors)
            visited.add(node)
            for neighbor in neighbors:
                if(neighbor not in visited):
                    dfs(neighbor)
            # return True
        
        components = 0
        for i in range(n):
            if(i not in visited):
                components += 1
                dfs(i)
        return components
