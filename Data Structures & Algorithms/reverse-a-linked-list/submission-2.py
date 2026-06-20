# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while(head is not None):
            print(head.val)
            stack.append(head)
            head = head.next

        head = stack[-1] if len(stack) > 0 else None
        for i in range(len(stack)-1, 0, -1):
            stack[i].next = stack[i-1]
        if len(stack) > 0:
            stack[0].next = None
        return head