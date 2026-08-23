class Solution:
    def helper(self, i, nums, curSub, finalSub):
        if i >= len(nums):
            finalSub.append(curSub.copy())
            return
        
        # We select nums[i]
        curSub.append(nums[i])
        self.helper(i + 1, nums, curSub, finalSub)
        curSub.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        self.helper(i + 1, nums, curSub, finalSub)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curSub, finalSub = [], []
        nums.sort()
        self.helper(0, nums, curSub, finalSub)
        return finalSub