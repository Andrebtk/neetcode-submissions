class Solution:
    def maxArea(self, heights: List[int]) -> int:
        MaxVolum = 0
        L, R = 0, len(heights) - 1



        while L < R:
            vol = min(heights[L], heights[R]) * (R - L)
            MaxVolum = max(MaxVolum, vol)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1


        return MaxVolum