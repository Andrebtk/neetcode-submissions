class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        M = {}
        for num in nums:
            M[num] = M.get(num, 0) + 1
        
        heap = []

        for num, count   in M.items():
            heapq.heappush(heap, [count, num])
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for _, val in heap:
            ans.append(val)
        
        return ans