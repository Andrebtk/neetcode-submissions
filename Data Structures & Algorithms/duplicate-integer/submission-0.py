class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for elem in nums:
            if seen.get(elem) is None:
                seen[elem] = True
            else:
                return True
        return False