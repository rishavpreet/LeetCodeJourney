'''
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.



Example 1:

Input: root = [1,null,2,2]
Output: [2]

Example 2:

Input: root = [0]
Output: [0]



Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -105 <= Node.val <= 105


Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to
 recursion does not count).
'''
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder(self, this_node):
        if this_node:
            if self.values.get(this_node.val) is not None:
                self.values[this_node.val] = self.values.get(this_node.val) + 1
            else:
                self.values[this_node.val] = 1
            self.preorder(this_node.left)
            self.preorder(this_node.right)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.values = {}
        self.preorder(root)
        root = None
        print(self.values)
        max_map = {}
        max_num = 0
        for key,val in self.values.items():
            if max_map.get(val) is not None:
                max_map[val].append(key)
            else:
                max_map[val] = [key]
            if val >= max_num:
                max_num = val
        if max_map.get(max_num) is not None:
            return max_map.get(max_num)
        else:
            return []


if __name__ == '__main__':
    sol = Solution()
    strs = ["flower", "flow", "flight"]
    output = "fl"
    result = sol.findMode(root=None)
    print(result)
    assert output == result
