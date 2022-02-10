class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        d1 = {}
        d2 = {}
        for i in range(len(s1)):
            d1[s1[i]] = d1.get(s1[i], 0) + 1
        print(d1, d2)
        for j in range(len(s2)):
            d2[s2[j]] = d2.get(s2[j], 0) + 1
            if j >= len(s1):
                d2[s2[j-len(s1)]] -= 1
                if d2[s2[j-len(s1)]] == 0:
                    d2.pop(s2[j-len(s1)])
            if d1 == d2:
                return True
            print(d2)
        return False
