class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        num = 0
        i = 0
        while(i<len(s)):
            if s[i:i+2]=='IV'or s[i:i+2]=='IX'or s[i:i+2]=='XL'or s[i:i+2]=='XC'or s[i:i+2]=='CD'or s[i:i+2]=='CM':
                num += dic[s[i:i+2]]
                i += 2
            else:
                num += dic[s[i]]
                i += 1
        return num


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        conver t ={'M': 1000 ,'D': 500 ,'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        ans = 0
        for i in range(len(s) - 1):
            if convert[s[i]] >= convert[s[i + 1]]:
                ans += convert[s[i]]
            else:
                ans = ans - convert[s[i]]
        return ans + convert[s[-1]]
