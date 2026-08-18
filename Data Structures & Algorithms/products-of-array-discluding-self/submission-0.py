class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd = [0] * len(nums)
        postProd = [0] * len(nums)

        total = 1
        i = 0
        for num in nums:
            total *= num
            preProd[i] = total
            i += 1
        
        total = 1
        for i in range(len(nums)-1, 0, -1):
            total *= nums[i]
            postProd[i] = total
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            L = preProd[i - 1] if i > 0 else 1
            R = postProd[i + 1] if i < len(nums) - 1 else 1
            res[i] = L * R


        return res