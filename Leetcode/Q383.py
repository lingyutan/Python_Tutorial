class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dr = Counter(ransomNote)
        dm = Counter(magazine)

        for key in dr.keys():
            if dr[key] > dm.get(key, 0):
                return False
        return True
