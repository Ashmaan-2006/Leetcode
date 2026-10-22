class Solution(object):
    def solve(self, board):

        if not board or not board[0]:
            return

        queue = deque()
        visited = set()

        rows, cols = len(board), len(board[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs():
            tracker = []
            touches_boundary = False

            while queue:
                row, col = queue.popleft()
                tracker.append((row, col))

                if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
                    touches_boundary = True

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        board[nr][nc] == 'O' and
                        (nr, nc) not in visited):

                        queue.append((nr, nc))
                        visited.add((nr, nc))

            if not touches_boundary:
                for row, col in tracker:
                    board[row][col] = 'X'

        for row in range(rows):
            for col in range(cols):

                if board[row][col] == 'O' and (row, col) not in visited:
                    queue.append((row, col))
                    visited.add((row, col))
                    bfs()