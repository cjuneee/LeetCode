class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        lis = []
        for i in range(num + 1):
            lenn = 0
            xx = bin(i)[2:]
            lenn = xx.count("1")
            lis.append(lenn)
        return lis


class Solution(object):
    def countBits1(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        r = [0]
        for i in range(1, num + 1):
            r.append(r[i & (i - 1)] + 1)
        return r

    def countBits(self, num):
        r = [0]
        base = 1
        while base <= num:
            next = base * 2
            for i in range(base, min(next, num + 1)):
                r.append(r[i - base] + 1)
            base = next
        return r