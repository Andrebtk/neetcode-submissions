class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1

        TopLeft = height[0]
        TopRight = height[-1]
        totalTrapped = 0

        while L < R:
            if TopLeft < TopRight:
                totalTrapped += min(TopLeft, TopRight) - height[L]
                L += 1
                TopLeft = max(TopLeft, height[L])
                
            else:
                totalTrapped += min(TopLeft, TopRight) - height[R]
                R -= 1
                TopRight = max(TopRight, height[R]) 

        return totalTrapped
