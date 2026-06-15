class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        li = 0
        ri = len(matrix) - 1

        while li <= ri:
            midi = (li + ri) // 2
            if target > matrix[midi][-1]:
                li = midi + 1
            elif target < matrix[midi][0]:
                ri = midi -1
            else:
                # target is in this row, now binary search the row
                l = 0
                r = len(matrix[midi])-1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[midi][mid] == target:
                        return True
                    elif matrix[midi][mid] > target:
                        r =  mid - 1
                    else:
                        l =   mid + 1
                return False

        return False