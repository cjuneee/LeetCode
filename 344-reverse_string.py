class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]




class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = "hello"
        t = ""
        for i, value in enumerate(s):
            t += s[len(s) - 1 - i]
        return t