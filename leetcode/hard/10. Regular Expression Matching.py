class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        memo = {}
        
        def dp(i, j):
            if tuple([i, j]) in memo:
                return memo[tuple([i, j])]

            if j == len(p):
                return i == len(s)
        
            first_match = i < len(s) and p[j] in {s[i], '.'}
            if j + 1 < len(p) and p[j + 1] == '*':
                memo[tuple([i, j])] = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                memo[tuple([i, j])] = first_match and dp(i + 1, j + 1)
            
            return memo[tuple([i, j])]
        
        return dp(0, 0)