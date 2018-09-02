class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        str = -1
        num = len(prices)
        for i in range(num):
            if str == -1 and i < num - 1:
                if i == 0 and prices[i] <= prices[i + 1]:
                    str = i
                if prices[i] <= prices[i - 1] and prices[i] < prices[i + 1]:
                    str = i
            if str != -1 and prices[i] >= prices[i - 1]:
                if i == num - 1:
                    total += prices[i] - prices[str]
                    str = -1
                elif prices[i] > prices[i + 1]:
                    total += prices[i] - prices[str]
                    str = -1
        return total


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        count = 0
        i = 1
        while i != n:
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                count += diff
            i += 1
        return count
