# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = head = ListNode()

        curr_list1 = list1
        curr_list2 = list2
        
        while curr_list1 and curr_list2:
            if curr_list1.val < curr_list2.val:
                curr.next = curr_list1
                curr_list1 = curr_list1.next
            else:
                curr.next = curr_list2
                curr_list2 = curr_list2.next
            curr = curr.next

        curr.next = curr_list1 or curr_list2


        return head.next






