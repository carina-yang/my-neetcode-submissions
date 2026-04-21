class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for x in range(9):
            for y in range(9):
                val = board[x][y]
                if val != ".":
                    box_id = ((x // 3) * 3) + (y // 3)

                    if val in col[y] or val in row[x] or val in box[box_id]:
                        return False
                    
                    col[y].add(val)
                    row[x].add(val)
                    box[box_id].add(val)


        return True