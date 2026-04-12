#Approach (BFS / DFS Coloring)
#1. Assign color 0 or 1 to each node
#2. Ensure neighbors always have opposite colors

class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n   # -1 = uncolored

        for i in range(n):
            if color[i] != -1:
                continue

            queue = deque([i])
            color[i] = 0

            while queue:
                node = queue.popleft()

                for nei in graph[node]:
                    # not colored → assign opposite color
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        queue.append(nei)

                    # conflict found
                    elif color[nei] == color[node]:
                        return False

        return True
