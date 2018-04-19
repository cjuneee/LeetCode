class Solution(object):
    def selfDividingNumbers(self, left, right):
        list1 = []
        pre_i = 0
        res = 0
        for i in range(left, right + 1):
            pre_i = i
            a = 0
            while (i != 0):
                res = i % 10
                if res != 0 and pre_i % res == 0:
                    a += 1
                i = i / 10
            if a == len(str(pre_i)):
                list1.append(pre_i)

        return list1
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
