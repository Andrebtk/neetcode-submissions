class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord('a') - ord(char)] += 1
            
            hashMap[tuple(count)].append(s)
        
        ans = []
        for _, val in hashMap.items():
            ans.append(val)
        
        return ans