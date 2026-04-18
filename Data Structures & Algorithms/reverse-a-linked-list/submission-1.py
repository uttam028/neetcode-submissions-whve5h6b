# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        if head is not None:
            while(head is not None):
                nodes.append(head)
                # print(head.val)
                head = head.next
                
            for i in range(len(nodes)-1, 0, -1):
                nodes[i].next = nodes[i-1]
            nodes[0].next=None
            head = nodes[-1]
        return head
