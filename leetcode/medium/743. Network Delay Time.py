class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        ans = 0

        for (node1, node2, dist) in times:
            graph[node1].append((dist, node2))

        visited = [False] * (n + 1)
        visited[k] = True
        visited_cnt = 1
        
        heap = []
        for node in graph[k]:
            heapq.heappush(heap, (node[0], node[1], k))
        
        dist_list = [float('inf')] * (n + 1)
        dist_list[k] = 0

        while visited_cnt < n and heap:
            (dist, next_node, from_node) = heapq.heappop(heap)
            if visited[next_node]:
                continue

            visited_cnt += 1
            visited[next_node] = True
            dist_list[next_node] = dist

            for node in graph[next_node]:
                if visited[node[1]]:
                    continue
                heapq.heappush(heap, (dist_list[next_node] + node[0], node[1], next_node))
        
        return -1 if visited_cnt != n else max(dist_list[1:])
        