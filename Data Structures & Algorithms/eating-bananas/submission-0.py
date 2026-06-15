class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kl = 1
        kr = max(piles)
        res = kr

        while kl <= kr:
            kmid = (kl + kr) // 2
            hours = 0
            for banan in piles:
                hours += math.ceil(banan / kmid)
            if hours <= h:
                res = kmid
                kr = kmid - 1
            else:
                kl = kmid + 1

        return res