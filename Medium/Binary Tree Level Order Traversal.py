'''
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000

'''
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import OrderedDict
class Solution:
    def helper(self, root:Optional[TreeNode], height:int):
        if not root:
            return None
        height += 1
        if self.hm.get(height) is not None:
            self.hm[height].append(root.val)
        else:
            self.hm[height] = [root.val]
        if root.left:
            self.helper(root.left, height)
        if root.right:
            self.helper(root.right, height)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        height = 0
        self.hm = OrderedDict()
        self.helper(root, height)
        return self.hm.values()