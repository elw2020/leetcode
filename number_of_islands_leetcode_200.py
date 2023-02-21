class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """ 
        def getIslandLength(node):
            stack = [node]
            while stack:
                row,col = stack.pop()
                if grid[row][col] == '*':
                    continue
                grid[row][col]='*'
                if row-1>=0 and grid[row-1][col]=='1':               # up
                    stack.append([row-1,col])
                if row+1<len(grid) and grid[row+1][col]=='1':        # down
                    stack.append([row+1,col])
                if col-1>=0 and grid[row][col-1]=='1':               # left
                    stack.append([row,col-1])
                if col+1 < len(grid[0]) and grid[row][col+1]=='1':   # right
                    stack.append([row,col+1])
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    getIslandLength([i,j])
                    numIslands+=1
        return numIslands
