class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        M = {}

        for i in range(len(nums)):
            num = nums[i]
            offset = target - num

            exist = M.get(offset)
            if exist is not None:
                return [exist, i]
            
            M[num] = i