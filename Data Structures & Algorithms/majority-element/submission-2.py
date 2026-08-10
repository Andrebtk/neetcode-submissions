class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority_count = n // 2

        data = dict()
        
        for elem in nums:
            count = data.get(elem)
            if count is None:
                data[elem] = 1
            else:
                data[elem] += 1
            
            if data[elem] > majority_count:
                    return elem