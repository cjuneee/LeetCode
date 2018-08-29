class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)):
            if A[i]>A[i-1] and A[i]>A[i+1]:
                return i


class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size = len(A)
        peak = 0
        for i in range(size - 1):
            if A[i] < A[i + 1]:
                peak = i + 1
            else:
                break;
        return peak

