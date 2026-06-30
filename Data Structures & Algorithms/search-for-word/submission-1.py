class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        if len(word) > ROWS * COLS:
            return False
        
        visit = set()

        def dfs(r, c, character):
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] != word[character]:
                return False
            if character == len(word) - 1:
                return True
            
            visit.add((r, c))
            
            res = (dfs(r + 1, c, character + 1)
                or dfs(r - 1, c, character + 1)
                or dfs(r, c + 1, character + 1)
                or dfs(r, c - 1, character + 1))

            visit.remove((r, c))

            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
                    
        return False

