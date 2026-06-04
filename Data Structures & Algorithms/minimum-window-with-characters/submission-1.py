class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l = 0
        window = {}
        tf = {}

        for char in t:
            tf[char] = tf.get(char, 0) + 1
        
        have = 0
        need = len(tf)

        for r in range(len(s)):
            if s[r] in tf:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == tf[s[r]]:
                    have += 1

            while have == need:
                if not res or (r - l + 1) < len(res):
                    res = s[l:r+1]
                
                if s[l] in tf:
                    window[s[l]] -= 1
                    if window[s[l]] < tf[s[l]]:
                        have -= 1
                l += 1

        return res