from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxArea = 0

        while left < right:
            width = right - left
            currentArea = width * min(height[left], height[right])

            if currentArea > maxArea:
                maxArea = currentArea

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea