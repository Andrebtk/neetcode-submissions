class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        memo = [-1] * N
    

        def aux(i):
            if i >= N:
                return 0

            if memo[i] == -1:
                memo[i] = max(aux(i + 1), nums[i] + aux(i + 2)) 
            
            return memo[i]
        


        return aux(0)