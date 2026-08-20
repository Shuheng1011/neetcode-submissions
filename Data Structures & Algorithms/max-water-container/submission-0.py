class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        top = 0
        bot = len(heights) - 1

        while top < bot:
            cur = min([heights[top], heights[bot]]) * (bot - top)

            if cur > max:
                max = cur

            if heights[top] > heights[bot]:
                bot = bot - 1

            else:
                top = top + 1
            

        return max
        