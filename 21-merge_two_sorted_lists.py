# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        new = ListNode(0)
        l3 = new
        while(l1 and l2):
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        l3.next = l1 or l2
        # if l1 == None:
        #     l3.next = l2
        # else:
        #     l3.next = l1
        return new.next