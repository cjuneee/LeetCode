class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        length = len(A)
        B = [[1]*length for i in range(length)]
        for i in range(length):
            for j  in range(length):
                B[i][j] -= A[i][length -1 -j]
        return B





class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i].reverse()
            for j in range(len(A[i])):
                if(A[i][j]==0):
                    A[i][j]=1
                else:
                    A[i][j]=0
        return(A)