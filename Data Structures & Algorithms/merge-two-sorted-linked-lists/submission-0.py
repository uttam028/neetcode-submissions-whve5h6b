# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        head = None
        while(list1 is not None or list2 is not None):
            if(list1 is not None and list2 is not None):
                if(list1.val < list2.val):
                    nodes.append(list1)
                    list1 = list1.next
                else:
                    nodes.append(list2)
                    list2 = list2.next
            elif(list1 is not None):
                nodes.append(list1)
                list1 = list1.next
            else:
                nodes.append(list2)
                list2 = list2.next
        if(len(nodes) >0):
            head = nodes[0]
            nodes[-1].next = None
            for i in range(len(nodes)-1):
                nodes[i].next = nodes[i+1]
        return head
