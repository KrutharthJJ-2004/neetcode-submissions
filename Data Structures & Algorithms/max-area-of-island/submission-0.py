class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0

        def sink(r,c):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c]!=1:
                return 0
            grid[r][c]=0
            return(1
                + sink(r+1,c)
                + sink(r-1,c)
                + sink(r,c+1)
                + sink(r,c-1))

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    count=max(count,sink(r,c))
        return count