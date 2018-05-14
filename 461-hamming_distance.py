class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = 0
        xx = bin(x)[2:]
        yy = bin(y)[2:]
        length = max(len(xx), len(yy))
        if length != len(xx):
            xx = xx.zfill(length)
        elif length != len(yy):
            yy = yy.zfill(length)
        for i in range(length):
            if xx[i] != yy[i]:
                n += 1

        return n


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        diff = x ^ y
        ret = 0
        while diff:
            diff &= diff - 1
            ret += 1
        return ret
