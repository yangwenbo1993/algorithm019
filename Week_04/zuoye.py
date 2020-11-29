#1.岛屿数量

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        self.length = len(grid)
        if self.length == 0:
            return 0
        self.width = len(grid[0])
        for i in range(0,self.length):
            for j in range(0,self.width):
                if grid[i][j] == '1':
                    count+=1
                    self.dfs(grid,i,j)
        return count

    def dfs(self,grid:List[List[str]],i:int,j:int):
        if i<0 or j<0 or i>=self.length or j>=self.width or grid[i][j]!='1':
            return
        grid[i][j] = '0'
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)


#2.搜索二维矩阵  二分查找

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0])
        up, down = 0, row - 1
        left, right = 0, col - 1
        while up <= down:
            rmid = (down + up) // 2
            if matrix[rmid][0] == target:
                return True
            elif matrix[rmid][0] < target:
                up = rmid + 1
            elif matrix[rmid][0] < target <= matrix[rmid][col - 1]:
                break
            else:
                down = rmid - 1

        while left <= right:
            cmid = (right + left) // 2
            if matrix[rmid][cmid] == target:
                return True
            elif matrix[rmid][cmid] < target:
                left = cmid + 1
            else:
                right = cmid - 1

        return False
