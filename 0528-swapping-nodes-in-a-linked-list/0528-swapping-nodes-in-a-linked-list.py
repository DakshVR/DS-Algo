# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        for _ in range(k-1):
            current = current.next
        
        first_node = current

        second = head
        temp = current

        while temp.next:
            temp = temp.next
            second = second.next
        
        second_node = second

        first_node.val, second_node.val = second_node.val, first_node.val

        return head


