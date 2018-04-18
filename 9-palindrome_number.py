class Solution(object):
    def isPalindrome(self, x):
        res = 0
        pre_x = x
        if x<0:
            return False
        else:
            while(x!=0):
                res = res*10 + x%10
                x = x/10
            return pre_x == res
        """
        :type x: int
        :rtype: bool
        """