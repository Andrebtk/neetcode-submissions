class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for elem in nums:
            count[elem] = 1 + count.get(elem, 0)
        
        heap = []
        heapq.heapify(heap)

        dist = set()

        for elem in nums:
            if elem not in dist:
                c = count[elem]
                
                heapq.heappush(heap, (c, elem))
                if len(heap) > k:
                    heapq.heappop(heap)
                dist.add(elem)
        
        ans = []
        for c, elem in heap:
            ans.append(elem)
        
        return ans


            