class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i in range(len(nums)):
            newT = target - nums[i]
            if m.get(newT) is not None:
                return [m.get(newT), i]
            m[nums[i]] = i
        
