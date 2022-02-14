class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1]]
        count = 2
        while count <= numRows:
            tmp = [1] * count
            for i in range(count-2):
                tmp[i+1] = res[count-2][i] + res[count-2][i+1]
            res.append(tmp)
            count += 1

        return res

            
