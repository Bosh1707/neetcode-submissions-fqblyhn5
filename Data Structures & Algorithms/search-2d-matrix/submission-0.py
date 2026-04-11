class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_lst = 0
        bot_lst = len(matrix) - 1
        l = 0
        r = len(matrix[0]) - 1
        while top_lst <= bot_lst:
            row = (top_lst + bot_lst) // 2
            if target > matrix[row][-1]:
                top_lst = row + 1
            elif target < matrix[row][0]:
                bot_lst = row - 1
            else:
                break
        
        if top_lst > bot_lst:
            return False

        row = (top_lst + bot_lst) // 2

        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return False


