class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        if len(word) > ROWS * COLS:
            return False

        def dfs(r, c, visit, character):
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] != word[character]:
                return False
            if character == len(word) - 1:
                return True
            
            visit.add((r, c))
            
            res = (dfs(r + 1, c, visit, character + 1)
                or dfs(r - 1, c, visit, character + 1)
                or dfs(r, c + 1, visit, character + 1)
                or dfs(r, c - 1, visit, character + 1))

            visit.remove((r, c))

            return res
        
        visit = set()
        character = 0
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, visit, character):
                    return True
                    
        return False

