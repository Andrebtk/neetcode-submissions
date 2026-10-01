class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        L, R = 0, len(heights) - 1



        while L < R:
            vol = min(heights[L], heights[R]) * (R - L)
            maxArea = max(maxArea, vol)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return maxArea