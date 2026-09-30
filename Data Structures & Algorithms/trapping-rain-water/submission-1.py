class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
    
        totalWater = 0
        topLeft = height[0]
        topRight = height[-1]

        while L < R:

            if topLeft < topRight:
                totalWater += min(topLeft, topRight) - height[L]
                L += 1
                topLeft = max(topLeft, height[L])
            else:
                totalWater += min(topLeft, topRight) - height[R]
                R -= 1
                topRight = max(topRight, height[R])
        

        return totalWater