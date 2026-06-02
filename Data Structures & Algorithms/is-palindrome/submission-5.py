class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        i = 0
        while i < len(s) - i - 1:
            if s[i] != s[len(s)-i-1]:
                return False
            i += 1
        return True
