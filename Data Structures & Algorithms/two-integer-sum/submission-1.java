class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++)
        {
            int compliment = target - nums[i];
            Integer inmap = map.get(nums[i]);
            if(inmap == null )
            {
                map.put(compliment,i);
            }
            else
            {
                int[] arr = {inmap, i};
                return arr;
            }
        }
        return null;
    }
}
