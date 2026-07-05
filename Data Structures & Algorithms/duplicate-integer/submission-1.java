class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        for(int num : nums)
        {
            if (seen.add(num) == false)
            {
                return true;
            }

        }
        return false;
}
}