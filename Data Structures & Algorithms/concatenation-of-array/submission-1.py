class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * (N * 2)
        
        for i in range(2):
            for j in range(N):
                ans[j + ((i-1) * N)] = nums[j]
            

        return ans