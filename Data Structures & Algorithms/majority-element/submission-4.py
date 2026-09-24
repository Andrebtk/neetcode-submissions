class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        M = len(nums) // 2

        hashMap = {}

        for elem in nums:
            val = hashMap.get(elem)
            if val is None:
                hashMap[elem] = 1
            else:
                hashMap[elem] += 1
            
            if hashMap[elem] > M:
                return elem
