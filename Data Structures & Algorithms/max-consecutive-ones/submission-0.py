class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_consecutive = 0
        current_consecutive = 0
        
        for num in nums:
            if num == 1:
                current_consecutive += 1
            else:
                current_consecutive = 0
            
            if max_consecutive < current_consecutive:
                max_consecutive = current_consecutive
        return max_consecutive

