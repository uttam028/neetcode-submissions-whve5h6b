class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for _ in range(numCourses)]

        for pre in prerequisites:
            adj[pre[0]].append(pre[1])
        
        visited = set()
        path = set()

        def has_cycle(node:int)-> bool:
            if(node in path):
                return True
            if(node in visited):
                return False
            
            path.add(node)
            for nei in adj[node]:
                if(has_cycle(nei)):
                    return True
            
            path.remove(node)
            visited.add(node)
            return False
        

        for i in range(numCourses):
            if(has_cycle(i)):
                return False
        return True
