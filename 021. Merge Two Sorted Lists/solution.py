# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = current_node = ListNode(0)

        while l1 != None or l2 != None:
            if l1 == None:
                current_node.next = l2
                break
            elif l2 == None:
                current_node.next = l1
                break

            if l1.val > l2.val:
                current_node.next = l2
                l2 = l2.next
            else:
                current_node.next = l1
                l1 = l1.next
            current_node = current_node.next

        return result.next
