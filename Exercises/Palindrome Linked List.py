# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#simple solution with O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        left , right = 0, len(stack)-1
        while left <= right:
            if stack[left] != stack[right]:
                return False
            left += 1
            right -= 1
        return True


#se volessi farlo in o(1) di spazio devo:
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #trovare la metà
        slow, fast = head,head
        while fast and fast.next:
            fast= fast.next.next
            slow = slow.next

        #reversare la lista
        prec = None
        while slow:
            tmp = slow.next
            slow.next = prec
            prec = slow
            slow = tmp

        #comparare
        left, right = head, prec
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True