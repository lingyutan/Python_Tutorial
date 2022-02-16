# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        res = ListNode(val = head.val, next = None)
        while head.next:
            res = ListNode(val = head.next.val, next = res)
            head = head.next
        return res
