class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, self.DFS(grid, i, j, 0))
        return max_area

    def DFS(self, grid:List[List[int]], i:int, j:int, count:int) -> int:
        while 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            count += 1
            grid[i][j] = 0
            for d in [[-1,0], [1,0], [0,-1], [0,1]]:
                count = self.DFS(grid, i + d[0], j + d[1], count)
        return count


        
