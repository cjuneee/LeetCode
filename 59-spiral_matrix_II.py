class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for i in range(n)]
        def genn(matrix,x,start,n):
            if (n <= 0):
                return
            if (n == 1):
                matrix[x][x] = start
                return
            for i in range(x,n+x):
                matrix[x][i] = start
                start += 1
            for i in range(x,n+x-1):
                matrix[i+1][n+x-1] = start
                start += 1
            for i in range(n+x-1,x,-1):
                matrix[n+x-1][i-1] = start
                start +=1
            for i in range(n+x-2,x,-1):
                matrix[i][x] = start
                start += 1
            genn(matrix,x+1,start,n-2)
        genn(matrix,0,1,n)
        return matrix



class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(0)
            result.append(temp)
        dim = n
        begin = 0
        count = 1
        while dim > 0:
            i = begin
            j = begin
            for k in range(dim):
                result[i][j + k] = count
                count += 1
            for k in range(1, dim):
                result[i + k][j + dim - 1] = count
                count += 1
            for k in range(1, dim):
                result[i + dim - 1][j + dim - 1 - k] = count
                count += 1
            for k in range(1, dim - 1):
                result[i + dim - 1 - k][j] = count
                count += 1
            dim -= 2
            begin += 1
        return result