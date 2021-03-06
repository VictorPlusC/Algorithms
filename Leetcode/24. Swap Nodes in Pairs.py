"""
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            first = head
            second = head.next
            
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
            head = first.next
        
        return dummy.next
