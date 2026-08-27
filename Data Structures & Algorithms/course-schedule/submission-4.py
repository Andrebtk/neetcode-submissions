class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prep = {i : [] for i in range(numCourses)}
        for a, b in prerequisites:
            prep[a].append(b)
        

        visited = set()

        def dfs(module):
            if module in visited:
                return False
            
            visited.add(module)
            for pre in prep[module]:
                if not dfs(pre):
                    return False
            visited.remove(module)
            prep[module] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
