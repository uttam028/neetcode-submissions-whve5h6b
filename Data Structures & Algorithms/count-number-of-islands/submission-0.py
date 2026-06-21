class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nodes = []
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == "1"):
                    nodes.append((i, j))

        def is_adjacent(a, b):
            # return abs(a[0]-b[0]) < 2 and abs(a[1]-b[1])<2
            return abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1


        print(nodes)

        graph = [[] for x in nodes]

        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                if(is_adjacent(nodes[i], nodes[j])):
                    graph[i] += [j]
                    graph[j] += [i]

        visited = set()
        def bfs(root):
            q = deque()
            q.append(root)
            while(len(q) > 0):
                curr = q.pop()
                visited.add(curr)
                neighbors = graph[curr]
                for neighbor in neighbors:
                    if(neighbor not in visited):
                        q.append(neighbor)

        components = 0

        for i in range(len(graph)):
            if(i not in visited):
                components +=1
                bfs(i)
        return components