# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current_node = result = ListNode(0)
        flag = 0

        while l1 is not None or l2 is not None or flag:
            current_val = flag
            if l1 is not None:
                current_val += l1.val
                l1 = l1.next
            if l2 is not None:
                current_val += l2.val
                l2 = l2.next
            flag = current_val // 10
            current_node.next = ListNode(current_val % 10)
            current_node = current_node.next

        return result.next
