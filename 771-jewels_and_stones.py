class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        i = 0
        for x in J:
            for j in range(len(S)):
                if x == S[j]:
                    i += 1
        return i


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return len([stone for stone in S if stone in J])