'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.



Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.



Constraints:

    The number of nodes in the list is in the range [1, 100].
    1 <= Node.val <= 100


'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from math import ceil


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = 0
        tail = head
        if not tail.next:
            return head
        while tail.next:
            res += 1
            tail = tail.next
        l = 0
        tail = head
        mid = ceil(res / 2)
        print(mid)
        while tail.next:
            l += 1
            if l == mid:
                return tail.next
            else:
                tail = tail.next


# using slow and fast pointer when fast reaches end slow will be in middle
# slow moves 1 step and fast moves 2 steps
class SolutionTwo:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        if not slow.next:
            return head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
