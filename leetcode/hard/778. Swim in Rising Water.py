class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        lo, hi = 0, n * n

        while lo < hi:
            mid = (lo + hi) // 2
            if self.canReach(grid, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def canReach(self, grid, time):
        if grid[0][0] > time:
            return False
        n = len(grid)
        reachable = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] <= time:
                    reachable[i][j] = True
        
        visited = set()
        def dfs(i, j):
            if i == n - 1 and j == n - 1:
                return True
            
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = i + dx, j + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                
                if reachable[nx][ny] and not (nx, ny) in visited:
                    visited.add((nx, ny))
                    if dfs(nx, ny):
                        return True

            return False

            
        visited.add((0, 0))
        return dfs(0, 0)