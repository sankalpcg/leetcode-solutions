class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        targetRow = -1
        for i in range(0,m):
            if matrix[i][0]>target:
                targetRow = i-1
                break
            if targetRow == -1:
                targetRow = m - 1

        start, end = 0, n-1
        while start<=end:
            mid = int(floor((start+end)/2))
            if target == matrix[targetRow][mid]:
                return True
            elif target>matrix[targetRow][mid]:
                start = mid+1
            elif target<matrix[targetRow][mid]:
                end = mid-1
        else:
            return False