# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
            if fast.next is not None:
                fast = fast.next
        return slow
