class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edge_used = 0
        ans = 0

        in_mst = [False] * n
        min_dist_list = [float('inf')] * n
        min_dist_list[0] = 0

        while edge_used < n:
            min_dist = float('inf')
            cur = -1

            for i in range(n):
                if not in_mst[i] and min_dist > min_dist_list[i]:
                    cur = i
                    min_dist = min_dist_list[i]

            in_mst[cur] = True
            ans += min_dist
            edge_used += 1

            for i in range(n):
                if in_mst[i]:
                    continue
                
                next_dist = abs(points[cur][0] - points[i][0]) + abs(points[cur][1] - points[i][1])
                if min_dist_list[i] > next_dist:
                    min_dist_list[i] = next_dist
            

        return ans