class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        memo = [-1] * (N + 1)


        def aux(i):
            if i >= N:
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(aux(i + 1), aux(i + 2) + nums[i])
            return memo[i]

        return aux(0)