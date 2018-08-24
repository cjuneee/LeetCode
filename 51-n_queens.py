class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [-1 for i in range(n)]
        def check(k, j):
            for i in range(k):
                if board[i] == j or abs(k-i) == abs(board[i]-j):
                    return False
            return True

        def dfs(depth, valuelist):
            if depth == n:
                res.append(valuelist)
                return
            for i in range(n):
                if check(depth, i):
                    board[depth] = i
                    s = '.' * n
                    dfs(depth+1, valuelist+[s[:i]+'Q'+s[i+1:]])
        dfs(0,[])
        return res



class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def DFS(queens,xy_diff,xy_sum):
            p=len(queens)
            if p==n:
                ans.append(queens)
                return
            #q表示新的皇后所在的列
            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    DFS(queens+[q],xy_diff+[p-q],xy_sum+[p+q])
        ans=[]
        DFS([],[],[])
        return [['.'*i+'Q'+'.'*(n-1-i) for i in sol] for sol in ans]














