class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)

        for s in strs:
            alpha = [0] * 26
            for letter in s:
                alpha[ord(letter) - ord('a')] += 1

            hashMap[tuple(alpha)].append(s)
        
        return list(hashMap.values())
