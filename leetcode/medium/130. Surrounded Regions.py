class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n, m = len(board), len(board[0])

        def dfs(row, col):
            if row < 0 or row >= n or col < 0 or col >= m:
                return
            if board[row][col] != 'O':
                return
            
            board[row][col] = 'M'
            
            for dx, dy in [(0, 1),(0, -1),(1, 0),(-1, 0)]:
                nx, ny = row + dx, col + dy
                dfs(nx, ny)
            
            return

        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)            
            if board[i][m - 1] == 'O':
                dfs(i, m - 1)
        
        for i in range(m):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[n - 1][i] == 'O':
                dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'M':
                    board[i][j] = 'O'

        return board