class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]

        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1

        for i in range(1, n):
            for k in dp[i - 1].keys():
                dp[i][k + nums[i]] = dp[i][k + nums[i]] + dp[i - 1][k]
                dp[i][k - nums[i]] = dp[i][k - nums[i]] + dp[i - 1][k]
        
        return dp[n-1][target]
