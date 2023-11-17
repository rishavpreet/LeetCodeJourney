'''
Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []



Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000



Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## iterative approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        tail = head
        prev = ListNode(val=head.val)
        while tail.next:
            temp = tail.next
            if temp:
                temp = ListNode(val=temp.val, next=prev)
                prev = temp
            tail = tail.next
        return prev


## recursive approach
class SolutionTwo:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        tail = head
        result = {'prev': ListNode(val=head.val)}

        def helper(tail, result):
            temp = tail.next
            if temp:
                temp = ListNode(val=temp.val, next=result['prev'])
                result['prev'] = temp
                return helper(tail.next, result)
            else:
                return None

        helper(tail, result)
        return result['prev']
