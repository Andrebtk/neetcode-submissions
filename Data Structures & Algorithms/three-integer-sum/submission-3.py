class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []


        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            L, R = i + 1, len(nums) - 1
            while L < R:
                threeSum = a + nums[L] + nums[R]
                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    ans.append([a, nums[L], nums[R]])
                    R -= 1
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return ans