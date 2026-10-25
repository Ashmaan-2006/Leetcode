class Solution(object):
    def minimumEffortPath(self, heights):
        
        rows = len(heights)
        cols = len(heights[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        heap = [(0, 0, 0)]

        best = []

        for r in range(rows):
                best.append([float('inf')] * cols)

        best[0][0] = 0

        while heap:

            effort, row, col = heapq.heappop(heap)

            if effort > best[row][col]:
                continue

            if row == rows - 1 and col == cols - 1:
                return effort

            for dr, dc in directions:

                if not (0 <= row + dr < rows) or not (0 <= col + dc < cols):
                    continue

                newEffort = max(effort, abs(heights[row + dr][col + dc] - heights[row][col]))

                if newEffort < best[row + dr][col + dc]:

                    best[row + dr][col + dc] = newEffort

                    heapq.heappush(heap, (newEffort, row + dr, col + dc))

                    

