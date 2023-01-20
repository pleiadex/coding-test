from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      def visit(i, j):
        # out of range
        # if i < 0 or len(grid) <= i or j < 0 or len(grid[0]) <= j:
        if not i in range(len(grid)) or not j in range(len(grid[0])):
          return

        if grid[i][j] == '0':
          return

        grid[i][j] = '0'
        visit(i + 1, j)
        visit(i - 1, j)
        visit(i, j + 1)
        visit(i, j - 1)
      
      res = 0
      for i in range(len(grid)):
        for j in range(len(grid[0])):
          if grid[i][j] == '1':
            res += 1
            visit(i, j)

      return res