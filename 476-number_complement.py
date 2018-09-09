class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        y = 0
        to2 = bin(num)
        for i in range(len(to2)-2):
            y += 10**i
        x = int(to2[2:])
        z = int(str(y-x),2)
        return z




class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 2**(len(bin(num))-2)-1-num     