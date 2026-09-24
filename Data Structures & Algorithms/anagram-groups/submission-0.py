class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = {}

        for s in strs:
            sortedS = ''.join(sorted(s))
            data = hashMap.get(sortedS)

            if data is not None:
                hashMap[sortedS].append(s)
            else:
                hashMap[sortedS] = [s]

        ans = []
        for key, values in hashMap.items():
            ans.append(values)
        
        return ans