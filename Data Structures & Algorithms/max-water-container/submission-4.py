class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        L, R = 0, N - 1

        maxVolume = 0

        while L < R:
            currVolume = (R - L) * (min(heights[L], heights[R]))
            maxVolume = max(maxVolume, currVolume)

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return maxVolume