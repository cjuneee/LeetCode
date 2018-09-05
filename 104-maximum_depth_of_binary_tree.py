# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        ll = rr = 0
        ll += self.maxDepth(root.left)
        rr += self.maxDepth(root.right)
        return max(ll, rr) + 1



class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root==None):
            return 0
        else:
            maxleft  = self.maxDepth(root.left)
            maxright = self.maxDepth(root.right)
        if(maxleft>maxright):
            return maxleft+1
        else:
            return maxright+1