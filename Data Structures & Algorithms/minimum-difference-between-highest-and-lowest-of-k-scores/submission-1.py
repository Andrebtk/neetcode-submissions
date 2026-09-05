class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        L = 0
        minScore = float('inf')

        for R in range(k - 1, len(nums)):
            minScore = min(minScore, nums[R] - nums[L])
            L += 1
        
        return minScore