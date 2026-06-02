class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set()
        for num in nums:
            hs.add(num)
        count = 0
        prev = 0
        for num in nums:
            if num - 1 not in hs:  # start of a sequence
                length = 1
                while num + length in hs:
                    length += 1
                count = max(count, length)
        return count