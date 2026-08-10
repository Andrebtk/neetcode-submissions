class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs)
        res = 0

        for index in range(len(min(strs[0], strs[-1]))):
            if strs[0][index] != strs[-1][index]:
                return strs[0][:res]
            else:
                res += 1
        return strs[0][:res]