# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        riporto = 0
        final = None
        head = final
        # se entrambi sono validi sommo ogni valore e controllo
        while l1 and l2:

            if not final:
                final = ListNode((l1.val + l2.val) % 10)
                head = final
            else:
                final.next = ListNode((l1.val + l2.val+ riporto) % 10 )
                final = final.next

            riporto = (l1.val + l2.val + riporto) // 10
            l1 = l1.next
            l2 = l2.next

        # altrimenti inserisco l'intera linkedlist rimasta
        while l1:
            val = (l1.val + riporto)
            l1.val = val % 10
            riporto = val // 10
            final.next = l1
            final = final.next
            l1 = l1.next

        while l2:
            val = (l2.val + riporto)
            l2.val = val % 10
            riporto = val // 10
            final.next = l2
            final = final.next
            l2 = l2.next

        if riporto == 0:
            final.next = None
        else:
            final.next = ListNode(riporto)
            final.next.next = None
        return head


sol = Solution()

l1 = ListNode(3)
current = l1
for val in [7]:
    current.next = ListNode(val)
    current = current.next

l2 = ListNode(9)
current = l2
for val in [2]:
    current.next = ListNode(val)
    current = current.next

l3 = (sol.addTwoNumbers(l1, l2))
while l3:
    print(l3.val)
    l3 = l3.next
