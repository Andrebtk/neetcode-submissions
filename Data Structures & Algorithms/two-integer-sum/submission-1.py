class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for index in range(len(nums)):
            val = d.get(target - nums[index])
            if val is None:
                d[nums[index]] = index
            else:
                return [val, index]
