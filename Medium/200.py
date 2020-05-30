class Solution:
    
    def sinkIsland(self, grid, i, j):
        grid[i][j]=0

        if i-1>=0 and grid[i-1][j]=='1':
            self.sinkIsland(grid, i-1, j)
        if i+1<len(grid) and grid[i+1][j]=='1':
            self.sinkIsland(grid, i+1, j)
        if j-1>=0 and grid[i][j-1]=='1' :
            self.sinkIsland(grid, i, j-1)
        if j+1<len(grid[0]) and grid[i][j+1]=='1':
            self.sinkIsland(grid, i, j+1)
        return 1
        
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count=0
        
        if grid==[]:
            return 0

        while any('1' in row for row in grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]=='1':
                        self.sinkIsland(grid, i, j)
                        island_count+=1
                        
        return island_count
                
