class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        M = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord('a') - ord(char)] += 1
            
            M[tuple(count)].append(word)
        
        ans = []
        for _, elem in M.items():
            ans.append(elem)

        return ans