class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dir_row = [0, 1, 0, -1]
        dir_col = [1, 0, -1, 0]
        memo_ = [[0] * n for _ in range(m)]
        ans = 0

        def dfs(row, col, memo):
            if memo[row][col] != 0:
                return memo[row][col] + 1

            for i in range(4):
                next_row = row + dir_row[i]
                next_col = col + dir_col[i]
                if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
                    continue
                
                if matrix[row][col] < matrix[next_row][next_col]:
                    memo[row][col] = max(memo[row][col], dfs(next_row, next_col, memo))
            
            return memo[row][col] + 1
        
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j, memo_))
        
        return ans