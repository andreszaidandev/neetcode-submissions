class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range (len(nums)):
            num = nums[i]
            if nums[abs(nums[i])-1] < 0:
                return abs(num)
            nums[abs(nums[i])-1] *= -1