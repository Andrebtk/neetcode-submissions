class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = count = 0

        for elem in nums:
            if count == 0:
                res = elem
            
            if elem == res:
                count += 1
            else:
                count -= 1
        return res