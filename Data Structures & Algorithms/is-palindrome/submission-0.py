class Solution:
    def isPalindrome(self, s: str) -> bool:
        inputString = "".join(char.lower() for char in s if char.isalnum())
        m = len(inputString) // 2

        left = 0
        right = -1

        while left < m:
            if inputString[left] != inputString[right]:
                return False
            else:
                left += 1
                right -= 1
        return True