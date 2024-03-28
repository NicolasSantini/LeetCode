# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            curr = head
            pred = None
            while curr:
                succ = curr.next
                curr.next = pred
                pred = curr
                curr = succ

            return pred
        return head