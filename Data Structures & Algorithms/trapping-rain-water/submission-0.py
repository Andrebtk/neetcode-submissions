class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1

        trappedWater = 0
        leftTopMax, rightTopMax = height[0], height[-1]
        while L < R:
            if leftTopMax < rightTopMax:
                trappedWater += min(leftTopMax, rightTopMax) - height[L]
                L += 1
                leftTopMax = max(leftTopMax, height[L])
            else:
                trappedWater += min(leftTopMax, rightTopMax) - height[R]
                R -= 1
                rightTopMax = max(rightTopMax, height[R])
        

        return trappedWater

            

            

            