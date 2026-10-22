class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for u, v in prerequisites:
            graph[u].append(v)


        path = set()
        visited = set()

        def dfs(course):

            if course in path:
                return False

            if course in visited:
                return True

            path.add(course)

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            path.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True