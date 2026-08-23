class Solution:

    def helper(self, i, nums, curSub, subsets):
        if i >= len(nums):
            subsets.append(curSub.copy())
            return
        
        # We select nums[i]
        curSub.append(nums[i])
        self.helper(i + 1, nums, curSub, subsets)
        curSub.pop()

        # We do not select nums[i]
        self.helper(i + 1, nums, curSub, subsets)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSub, subsets = [], []
        self.helper(0, nums, curSub, subsets)
        return subsets