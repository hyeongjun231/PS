class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        reversed_graph = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            reversed_graph[a].append(b)
            
        queue = ['JFK']
        ans = []
        
        while queue:
            if reversed_graph[queue[-1]]:
                queue.append(reversed_graph[queue[-1]].pop())
            else:
                ans.append(queue.pop())
            
        return ans[::-1]
            