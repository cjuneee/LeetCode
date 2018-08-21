class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        output = [[]]
        for i in range(length):
            for j in range(len(output)):
                output.append(output[j]+[nums[i]])
        return output




class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        if len(nums) == 0:
            return res
        if len(nums) == 1:
            res.append(nums)
            return res
        else:
            res = self.subsets(nums[1:])
            ele = nums[0]
            for i in range(0, len(res)):
                res.append([ele] + res[i])
            return res