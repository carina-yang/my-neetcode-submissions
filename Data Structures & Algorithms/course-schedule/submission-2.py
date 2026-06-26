from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        
        queue = deque(course for course in range(numCourses) if in_degree[course] == 0)

        completed = 0
        while queue:
            course = queue.popleft()
            completed += 1

            for neighbour in graph[course]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        return completed == numCourses

