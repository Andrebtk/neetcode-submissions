# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        visited_nodes = dict()

        curr = head

        while curr != None:
            if visited_nodes.get(curr):
                return True
            
            visited_nodes[curr] = True
            curr = curr.next

        return False
