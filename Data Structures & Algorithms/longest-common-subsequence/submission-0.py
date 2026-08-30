class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        
        memo = [[-1] * M for i in range(N)]
        
        def aux(i1, i2):
            if i1 >= N or i2 >= M:
                return 0
            
            if memo[i1][i2] != -1:
                return memo[i1][i2]
            
            if text1[i1] == text2[i2]:
                memo[i1][i2] = 1 + aux(i1 + 1, i2 + 1)
            else:
                memo[i1][i2] = max(aux(i1 + 1, i2), aux(i1, i2 + 1))
            
            return memo[i1][i2]
            

        return aux(0, 0)