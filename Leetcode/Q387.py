class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if d.get(s[i], None) is not None:
                d[s[i]] = "Biu"
            else:
                d[s[i]] = i
        res = [x for x in d.values() if x != "Biu"]
        if res:
            return min(res)
        else:
            return -1
