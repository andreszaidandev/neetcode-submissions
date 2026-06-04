class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        window = {}
        maxfreq = 0
        result = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            maxfreq = max(maxfreq, window[s[r]])

            while (r - l + 1) - maxfreq > k:
                window[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result