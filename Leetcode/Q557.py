class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        res = []
        for word in s:
            res.append(word[::-1])
        return " ".join(res)


# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return " ".join(word[::-1] for word in s.split(" "))
