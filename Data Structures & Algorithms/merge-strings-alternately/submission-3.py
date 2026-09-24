class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        N, M = len(word1), len(word2)

        limit = min(N, M)
        ans = []

        for i in range(limit):
            ans.append(word1[i])
            ans.append(word2[i])
        
        ans.append(word1[limit:])
        ans.append(word2[limit:])

        return "".join(ans)