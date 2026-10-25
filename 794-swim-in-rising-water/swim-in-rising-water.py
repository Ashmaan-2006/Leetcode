class Solution(object):
    def swimInWater(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        heap = [(grid[0][0], 0, 0)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        maxheight = grid[0][0]

        visited = set()

        while heap:

            height, row, col = heapq.heappop(heap)

            if (row, col) in visited:
                continue

            else:
                visited.add((row, col))

            if row == rows - 1 and col == cols - 1:
                return height

            for dr, dc in directions:

                if not (0 <= row + dr < rows) or not (0 <= col + dc < cols):
                    continue

                maxheight = max(grid[row + dr][col + dc], height)

                heapq.heappush(heap, (maxheight, row + dr, col + dc))
        