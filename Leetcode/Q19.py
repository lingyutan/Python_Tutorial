# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        k = 0
        while fast:
            # If there is only one node, return none
            if not head.next:
                return None
            fast = fast.next
            k += 1
            # fast pointer reach the end, so delete slow.next
            if not fast:
                # if the node to be removed is the head, remove head
                if k == n:
                    head = head.next
                # else remove slow.next
                else:
                    slow.next = slow.next.next
            # update slow pointer
            if k > n:
                slow = slow.next
        return head
