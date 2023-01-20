from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      def visit(i, j):
        queue = deque()
        queue.append((i, j))

        while queue: 
          r, c = queue.popleft()
          
          if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == '1':
            grid[r][c] = '0'
            queue.append((r + 1, c))
            queue.append((r - 1, c))
            queue.append((r, c + 1))
            queue.append((r, c - 1))
      
      res = 0
      for i in range(len(grid)):
        for j in range(len(grid[0])):
          if grid[i][j] == '1':
            res += 1
            visit(i, j)

      return res