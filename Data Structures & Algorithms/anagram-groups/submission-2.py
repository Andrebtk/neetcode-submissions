class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            hashMap[sortedS].append(s)
            

        return list(hashMap.values())