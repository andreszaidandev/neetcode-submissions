class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rp = 1
        left =[]
        right = []
        for i in range(len(nums)):
            left.append(rp)
            rp = rp * nums[i]
        rp = 1

        for i in range(len(nums)-1, -1, -1):
            right.append(rp)
            rp = rp * nums[i]
        right = right[::-1]
        for i in range(len(nums)):
            nums[i] = left[i] * right[i]
        return nums