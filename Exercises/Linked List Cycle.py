# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#O(n) space O(n) time
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # devo tenere conto anche della posizione in cui inizia il ciclo
        pos = -1
        mappa = {}
        index = 0
        while head:
            if head in mappa:
                pos = mappa[head]
                return True
            else:
                mappa[head] = index
                index += 1
            head = head.next
        return False

#with the two pointers I can do it with O(1) memory

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pos = 0
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            pos += 1
            if slow == fast:
                return True
        return False