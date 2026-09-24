class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        N, M = len(word1), len(word2)

        ans = ""
        index1, index2 = 0, 0
        for i in range(min(N, M) * 2):

            if i%2 == 0:
                ans += word1[index1]
                index1 += 1
            else:
                ans += word2[index2]
                index2 += 1

        if index2 != M:
            ans += word2[index2:]
        
        if index1 != N:
            ans += word1[index1:]

        return ans