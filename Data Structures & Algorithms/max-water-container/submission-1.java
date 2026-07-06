class Solution {
    public int maxArea(int[] heights) {
     int l = 0;
     int r = heights.length - 1;
     int maxwater = 0;

        while (l < r)
        {
            if(heights[l] > heights[r])
            {
                maxwater = Math.max(maxwater, (r-l)*heights[r]);
                r--;
            }
            else if (heights[l] <= heights[r])
            {
                maxwater = Math.max(maxwater, (r-l)*heights[l]);
                l++;
            }
        }
        return maxwater;
    }
}
