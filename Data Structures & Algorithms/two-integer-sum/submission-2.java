class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> seen = new HashMap<Integer,Integer>();
        int[] res = new int[2];
        for(int i = 0; i < nums.length; i++)
        {
            int compliment = target - nums[i];

            if(seen.get(compliment) != null)
            {
                res[0] = seen.get(compliment);
                res[1] = i;
                break;
            }
            else
            {
                seen.put(nums[i],i);
            }
        }
        return res;

    }
}
