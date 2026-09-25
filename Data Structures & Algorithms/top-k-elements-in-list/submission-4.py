class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for elem in nums:
            count[elem] = 1 + count.get(elem, 0)
        
        
        heap = []

        for elem, c in count.items():
            heapq.heappush(heap, [c, elem])
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for c, elem in heap:
            ans.append(elem)

        return ans