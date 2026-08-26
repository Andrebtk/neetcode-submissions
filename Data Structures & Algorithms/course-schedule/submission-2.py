class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prepMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            prepMap[course].append(pre)

        visited = set()

        def dfs(cur):
            if cur in visited:
                return False
            


            # Not yet visited so no cycle
            visited.add(cur)
            for pre in prepMap[cur]:
                if not dfs(pre):
                    return False
            visited.remove(cur)
            prepMap[cur] = []
            
            return True
        

        for module in range(numCourses):
            if dfs(module) == False:
                return False
            
        return True
            
        




