class Solution {
    public int[] twoSum(int[] numbers, int target) {

        int r = numbers.length -1;
        int l = 0;
        int[] res = new int[2];

        while(l<r)
        {
            int sum = numbers[l] + numbers[r];
            if (target == numbers[l]+numbers[r])
            {
                res[0] = l+1;
                res[1] = r+1;
                break;
            }
            else if (target < sum)
            {
                r--;
            }
            else
            {
                l++;
            }
        }
        return res;
    }
}
