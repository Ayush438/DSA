# Cycle detection in directed graph


from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # build graph
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # queue for nodes with indegree 0
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count = 0

        while queue:
            node = queue.popleft()
            count += 1

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses
