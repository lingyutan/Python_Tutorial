class Solution:
    def isValid(self, s: str) -> bool:
        tmp = []
        for char in s:
            if char in ['(', '[', '{']:
                tmp.append(char)
            else:
                if tmp and abs(ord(char) - ord(tmp[-1])) <= 2:
                    tmp.pop()
                else:
                    return False
        if tmp:
            return False
        return True
