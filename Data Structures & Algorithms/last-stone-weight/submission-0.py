class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = [-s for s in stones]
        heapq.heapify(stone)

        while len(stone) > 1:
            x = -heapq.heappop(stone)
            y = -heapq.heappop(stone)
            newWeight = 0
            if x != y:
                if x < y:
                    newWeight = y - x
                else:
                    newWeight = x - y
            heapq.heappush(stone, -newWeight) 
        
        if len(stone) == 0:
            return 0
        else:
            return -stone[0]