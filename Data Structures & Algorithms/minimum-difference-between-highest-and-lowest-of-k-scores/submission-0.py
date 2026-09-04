class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minDiff = float("inf")
        
        L = 0
        for R in range(k - 1, len(nums)):
            minDiff = min(minDiff, nums[R] - nums[L])
            L += 1
        
        return minDiff

