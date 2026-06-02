class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = set()
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict.add(nums[i])
            else:
                return True
            
        return False