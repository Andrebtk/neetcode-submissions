class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        numberOfTimes = dict()

        for letter in s:
            if letter not in numberOfTimes:
                numberOfTimes[letter] = 1
            else:
                numberOfTimes[letter] += 1

        for letter in t:
            if letter not in numberOfTimes:
                return False
            else:
                numberOfTimes[letter] -= 1

                if numberOfTimes[letter] < 0:
                    return False
    

        return True
        
        