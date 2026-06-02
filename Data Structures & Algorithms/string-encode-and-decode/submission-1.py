class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for string in strs:
            for char in string:
                result.append(ord(char))
            result.append(-1)
        return str(result)
        
    def decode(self, s: str) -> List[str]:
        arr = []
        string = ""
        for char in eval(s):
            if char == -1:
                arr.append((string))
                string = ""
            else:
                string += chr(char)
        return arr