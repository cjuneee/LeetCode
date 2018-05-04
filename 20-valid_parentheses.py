class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = ['$']
      #  if len(s) % 2 != 0:
            # return (t != [])
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                t.append(s[i])
            elif s[i] == ')' and t[-1] == '(':
                t.pop()
            elif s[i] == '}' and t[-1] == '{':
                t.pop()
            elif s[i] == ']' and t[-1] == '[':
                t.pop()
            else:
                return False
        return (len(t) == 1)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = [None]
        parmap = {')':'(','}': '{', ']': '['}
        for c in s:
            if c in parmap:
                if parmap[c] != pars.pop():
                    return False
            else:
                pars.append(c)
        return len(pars) == 1


