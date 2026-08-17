class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        max_water = 0

        while L < R:
            if (R - L) * min(heights[L], heights[R]) > max_water:
                max_water = (R - L) * min(heights[L], heights[R])

            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
    
        return max_water