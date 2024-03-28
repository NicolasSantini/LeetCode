# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#space O(1) time O(n+m)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        final :ListNode = ListNode()
        head :ListNode = None
        while (list1 is not None and list2 is not None):
            if list1.val <= list2.val:
                final.next = list1
                list1 = list1.next
            else:
                final.next = list2
                list2 = list2.next

            final = final.next
            if head is None:
                head = final


        if list1 is None:
            final.next = list2
        if list2 is None:
            final.next = list1

        return head