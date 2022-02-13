class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        else:
            original = []
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    original. append(mat[i][j])
            res = []
            for i in range(r):
                tmp = []
                for j in range(c):
                    tmp.append(original[i*c+j])
                res.append(tmp)
            return res
        
