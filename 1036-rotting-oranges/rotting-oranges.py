
class Solution(object):
    def orangesRotting(self, grid):

        visited = set()
        count = 0
        minutes = 0
        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == 1:
                    count += 1

                if grid[row][col] == 2:
                    queue.append((row, col))

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while queue and count > 0:

            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:

                    if (0 <= row + dr < len(grid)
                        and 0 <= col + dc < len(grid[0])
                        and grid[row + dr][col + dc] == 1):

                        grid[row + dr][col + dc] = 2
                        queue.append((row + dr, col + dc))
                        count -= 1

            minutes += 1

        if count != 0:
            return -1
        else:
            return minutes