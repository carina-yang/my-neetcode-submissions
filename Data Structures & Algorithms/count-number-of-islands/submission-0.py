from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"

            while queue:
                x, y = queue.popleft()
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    if min(x + dr, y + dc) < 0 or x + dr == ROWS or y + dc == COLS or grid[x + dr][y + dc] == "0":
                        continue
                    queue.append((x + dr, y + dc))
                    grid[x + dr][y + dc] = "0"

        count = 0
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)

        return count