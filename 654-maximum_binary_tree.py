# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def helper(start, end):
            if start > end or start == len(nums):
                return None
            elif start == end:
                max_nums = nums[start]
            else:
                max_nums = max(nums[start:end + 1])
            max_i = nums.index(max_nums)
            node = TreeNode(max_nums)
            node.left = helper(start, max_i - 1)
            node.right = helper(max_i + 1, end)
            return node

        return helper(0, len(nums))

#范例1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        #就是简单的用递归构造二叉树
        if not nums:
            return None
        maxn=max(nums)
        max_ind=nums.index(maxn)
        root=TreeNode(maxn)
        root.left=self.constructMaximumBinaryTree(nums[:max_ind])
        root.right=self.constructMaximumBinaryTree(nums[max_ind+1:])
        return root


#范例2
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(s, e):
            if s > e:
                return None
            max = nums[s]
            max_index = s
            for i in range(s+1,e+1):
                if nums[i] > max:
                    max = nums[i]
                    max_index = i
            node = TreeNode(max)
            node.left = helper(s, max_index-1)
            node.right = helper(max_index+1, e)
            return node
        return helper(0, len(nums)-1)