class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        height = len(matrix)

        L = 0
        R = (width * height) - 1

        while L <= R:
            mid = (L + R) // 2

            x = mid % width
            y = mid // width

            if target < matrix[y][x]:
                R = mid - 1
            elif target > matrix[y][x]:
                L = mid + 1
            else:
                return True
        
        return False
