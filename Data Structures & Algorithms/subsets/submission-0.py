class Solution:

    def helper(self, i, nums, curSet, subsets):
        if i >= len(nums):
            subsets.append(curSet.copy())
            return
        
        # We select the nums[i]
        curSet.append(nums[i])
        self.helper(i+1, nums, curSet, subsets)
        curSet.pop()


        # We skip the nums[i]
        self.helper(i+1, nums, curSet, subsets)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSet, subsets = [], []
        self.helper(0, nums, curSet, subsets)
        return subsets