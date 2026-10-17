class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):

        graph = {}
        visited = set()
        
        for i in range(n):
            graph[i] = []

        for u, v, price in flights:
            graph[u].append((v, price))

        heap = [(0, src, 0)]

        while heap:

            cost, city, stops = heapq.heappop(heap)

            if city == dst:
                return cost

            if stops == k + 1:
                continue

            if (stops, city) in visited:
                continue

            visited.add((stops, city))

            for new_city, price in graph[city]:

                new_stops = stops + 1

                new_cost = cost + price

                heapq.heappush(heap, (new_cost, new_city, new_stops))

        return -1