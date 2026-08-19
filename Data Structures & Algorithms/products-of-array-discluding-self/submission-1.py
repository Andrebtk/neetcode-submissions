class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre = 1
        for index, num in enumerate(nums):
            res[index] = pre
            pre *= num
            
        
        post = 1
        for index in range(len(nums)-1, -1, -1):
            res[index] *= post 
            post *= nums[index]

        return res 
