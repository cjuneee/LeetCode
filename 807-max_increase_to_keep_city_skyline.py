class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = []
        col = []
        sum = 0
        length = len(grid)
        for i in range(length):
            row.append(max(grid[i]))
            col.append(max(x[i] for x in grid))
        for i in range(length):
            for j in range(length):
                 if grid[i][j] < row[i] and grid[i][j] < col[j]:
                        sum +=  min(row[i],col[j]) - grid[i][j]
        return sum


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = map(max, grid)
        col = map(max, zip(*grid))#取每一列构成新的矩阵
        #[(i, j) for i in row for j in col]是每一行列的最大值，用map(min,)构成新的矩阵，用sum求和，两个矩阵和相减
        return sum(map(min, [(i, j) for i in row for j in col])) - sum(map(sum, grid))
