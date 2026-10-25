class Solution(object):
    def networkDelayTime(self, times, n, k):

        graph = {}

        for i in range(1, n + 1):
            graph[i] = []

        for u, v, w in times:
            graph[u].append((v, w))

        dist = {}

        for i in range(1, n + 1):
            dist[i] = float('inf')

        dist[k] = 0

        heap = [(k, 0)]

        while heap:

            node, distance = heapq.heappop(heap)

            for neighbor, weight in graph[node]:

                new_distance = distance + weight

                if new_distance < dist[neighbor]:

                    dist[neighbor] = new_distance

                    heapq.heappush(heap, (neighbor, new_distance))


        answer = max(dist.values())

        if answer == float('inf'):
            return -1

        return answer

