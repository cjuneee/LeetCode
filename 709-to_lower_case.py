class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """

        res = ''
        for i in str:
            if i >= 'A' and i <= 'Z':
                res += chr(ord(i) - ord('A') + ord('a'))
            else:
                res += i
        return res


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()