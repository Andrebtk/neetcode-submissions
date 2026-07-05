class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenS = set()
        numberOfTimes = dict()

        for letter in s:
            seenS.add(letter)

            if letter not in numberOfTimes:
                numberOfTimes[letter] = 1
            else:
                numberOfTimes[letter] += 1

        for letter in t:
            if letter not in seenS:
                return False
            else:
                numberOfTimes[letter] -= 1

                if numberOfTimes[letter] < 0:
                    return False
        
        for val in numberOfTimes.values():
            if val != 0:
                return False
                
        return True
        
        