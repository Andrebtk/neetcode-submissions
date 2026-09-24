class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = {}
        hashMapT = {}



        for elem in s:
            if elem in hashMapS:
                hashMapS[elem] += 1
            else:
                hashMapS[elem] = 1
        
        for elem in t:
            if elem in hashMapT:
                 hashMapT[elem] += 1
            else:
                 hashMapT[elem] = 1
        
        for key, value in hashMapS.items():
            if hashMapT.get(key) is not None: 
                if hashMapT[key] != value:
                    return False
                del hashMapT[key]
            else:
                return False
        
        return hashMapT == {}

        