class Solution:

    def helper(self, i, nums, curSet, subSets):
        if i >= len(nums):
            subSets.append(curSet.copy())
            return
        
        # we select nums[i]
        curSet.append(nums[i])
        self.helper(i + 1, nums, curSet, subSets)
        curSet.pop()

        # We do not select nums[i]
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.helper(i + 1, nums, curSet, subSets)


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curSet, subSets = [], []
        self.helper(0, nums, curSet, subSets)
        return subSets