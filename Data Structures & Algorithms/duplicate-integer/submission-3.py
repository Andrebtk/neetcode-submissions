class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        M = set()


        for elem in nums:
            if elem in M:
                return True
            else:
                M.add(elem)

        return False