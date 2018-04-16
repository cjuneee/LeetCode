#执行时间更短
class Solution(object):
    def reverse(self, x):
        flag = 1 if x > 0 else -1
        res = 0
        x = abs(x)
        while (x != 0):
            res = res * 10 + x % 10
            x = x / 10
        res = flag * res
        return res if res < 2 ** 31 - 1 and res > -2 ** 31 else 0

#学习str(x)[::-1]
class Solution(object):
    def reverse(self, x):
        res = 0
        res = int(str(x)[::-1]) if x>=0 else - int(str(-x)[::-1])
        return res if res < 2**31-1 and res > -2**31 else 0

