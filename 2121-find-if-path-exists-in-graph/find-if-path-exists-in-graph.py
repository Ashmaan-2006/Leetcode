class Solution(object):
    def validPath(self, n, edges, source, destination):

        if source == destination:
            return True

        if not edges:
            return False

        graph = {}

        for i in range(n):
            graph[i] = []

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([source]) 

        seen = set([source])

        while queue:

            node = queue.popleft()

            if node == destination:
                return True
            
            for neighbor in graph[node]:

                if neighbor in seen:
                    continue

                else:
                    queue.append(neighbor)
                    seen.add(neighbor)

        return False






        # go through the queue, and find its neighbors, then append those neighbors to queue
        # - that works if everything is connected
        #    - that does not have to be the case

        # so we can have a loop that goes through all the range, and check all their neigbors

        #dont want to reiterate through a node, so use seen set
        