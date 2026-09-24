class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}
        for elem in nums:
            hashMap[elem] = 1 + hashMap.get(elem, 0)
        

        heap = []

        for num, nb in hashMap.items():
            heapq.heappush(heap, [nb, num])
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for _, num in heap:
            ans.append(num)
        
        return ans
