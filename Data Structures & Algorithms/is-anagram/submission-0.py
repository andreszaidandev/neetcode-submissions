class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            dict = {}
            for char in s:
                dict[char] = dict.get(char,0) +1
            for char in t:
                if char not in dict:
                    return False
                else:
                    dict[char] -= 1
                    if dict[char] == 0:
                        del dict[char]
            return len(dict) == 0
        