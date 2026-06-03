class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        maxwater= 0

        while i<j:
            if heights[i] > heights[j]:
                maxwater = max(maxwater, (j-i) *heights[j])
                j-=1
            if heights[i] <= heights[j]:
                maxwater = max(maxwater, (j-i)*heights[i])
                i+=1

        return maxwater