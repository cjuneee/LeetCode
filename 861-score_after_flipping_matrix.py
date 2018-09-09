class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        row = len(A)
        col = len(A[0])
        for i in range(row):
            if A[i][0] == 0:
                for j in range(col):
                    A[i][j] = 1- A[i][j]
        print A
        for i in range(col):
            num = 0
            for j in range(row):
                if A[j][i] == 0:
                    num += 1
            print row//2
            if num > row/2:
                for j in range(row):
                    A[j][i] = 1-A[j][i]
        print row,col,A
        total = 0
        for i in range(row):
            for j in range(col):
                total += A[i][j]*(2**(col-1-j))
        return total


class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def change(list):
            for i in range(len(list)):
                if list[i] == 0:
                    list[i] = 1
                else:
                    list[i] = 0
            return list

        for row in A:
            if row[0] == 0:
                change(row)
        zip_a = list(zip(*A))
        tmp = []
        for row in zip_a:
            if row.count(0) > row.count(1):
                row = change(list(row))
            tmp.append(row)
        result = list(zip(*tmp))
        res = 0
        for row in result:
            s = ''
            for i in row:
                s += str(i)
            res += int(s, 2)
        return res