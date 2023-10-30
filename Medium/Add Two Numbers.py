'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.


'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        ln = self
        result = []
        print("[", ln.val, end=",")
        result.append(ln.val)
        while ln.next is not None:
            ln = ln.next
            result.append(ln.val)
            print(ln.val, end=",")
        print("]")
        return str(result)


class SolutionOne:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        num1_s = str(l1.val)
        num1 = int(num1_s)
        while n1.next is not None:
            n1 = n1.next
            num1_s = str(n1.val) + num1_s
            num1 = int(num1_s)
        # print(num1)
        n2 = l2
        num2_s = str(l2.val)
        num2 = int(num2_s)
        while n2.next is not None:
            n2 = n2.next
            num2_s = str(n2.val) + num2_s
            num2 = int(num2_s)
        # print(num2)
        result = num1 + num2
        result_s = str(result)
        # print(result_s)
        prev_node = None
        result_l = ListNode()
        for c in result_s:
            result_l = ListNode(val=int(c), next=prev_node)
            prev_node = result_l
        return result_l


if __name__ == '__main__':
    sol = SolutionOne()
    l1 = ListNode(2, next=ListNode(4, next=ListNode(3, None)))
    l2 = ListNode(5, next=ListNode(6, next=ListNode(4, None)))
    output = str(ListNode(7, next=ListNode(0, next=ListNode(8, None))))
    result = str(sol.addTwoNumbers(l1, l2))
    print("out", output)
    print("res", str(result))
    assert output == result
