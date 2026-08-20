class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        newList = []
        for x,y in points:
            dist = x**2 + y**2
            newList.append([dist, x, y])
        
        
        heapq.heapify(newList)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(newList)
            res.append([x,y])
            k -= 1
        
        return res