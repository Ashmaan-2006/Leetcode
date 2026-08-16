class Solution(object):
    def numIslands(self, grid):

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def bfs (r, c):

            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while q: 

                r, c = q.popleft()

                for dr, dc in directions:

                    if ((dc + c) in range(len(grid[0])) and
                    (dr + r) in range(len(grid)) and 
                    grid[dr + r][dc + c] == "1" and 
                    (dr + r, dc + c) not in visit):

                        visit.add((dr + r, dc + c))
                        q.append((dr + r, dc + c))


        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1

                    bfs(r, c)

        return islands