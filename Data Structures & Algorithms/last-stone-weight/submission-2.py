class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        newStones = [-s for s in stones]

        heapq.heapify(newStones)

        while len(newStones) > 1:
            x = -heapq.heappop(newStones)
            y = -heapq.heappop(newStones)
            if x < y:
                heapq.heappush(newStones, -(y-x))
            if x > y:
                heapq.heappush(newStones, -(x-y))
        
        if len(newStones) > 0:
            return -newStones[0]
        else:
            return 0