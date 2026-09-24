class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = set()
        for elem in nums:
            if elem in m:
                return True
            m.add(elem)
        
        return False