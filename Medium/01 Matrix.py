'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]



Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 104
    1 <= m * n <= 104
    mat[i][j] is either 0 or 1.
    There is at least one 0 in mat.
'''
from typing import List

from queue import Queue


## using BFS and queue
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        queue = Queue()
        result = [[-1 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.put([i, j])

        while not queue.empty():
            i, j = queue.get()
            for dir_i, dir_j in directions:
                new_i = i + dir_i
                new_j = j + dir_j

                if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and result[new_i][new_j] == -1:
                    result[new_i][new_j] = result[i][j] + 1
                    queue.put([new_i, new_j])

        return result


## using DP
class SolutionTwo:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    mat[i][j] = m + n
                    if i > 0:
                        mat[i][j] = min(mat[i - 1][j] + 1, mat[i][j])
                    if j > 0:
                        mat[i][j] = min(mat[i][j - 1] + 1, mat[i][j])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] != 0:
                    if i + 1 < m:
                        mat[i][j] = min(mat[i + 1][j] + 1, mat[i][j])
                    if j + 1 < n:
                        mat[i][j] = min(mat[i][j + 1] + 1, mat[i][j])
        return mat
