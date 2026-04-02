# Cycle detection in directed graph
#(DFS Cycle Detection)
Use 3 states:
0 = unvisited
1 = visiting (cycle detection)
2 = visited
Run DFS; if a node is revisited while state = 1, a cycle exists.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph=defaultdict(list)
        for i,j in prerequisites:
            graph[j].append(i)

        state=[0]*numCourses

        def dfs(node):
            if state[node]==1:
                return True
            if state[node]==2:
                return False

            state[node]=1
            for nei in graph[node]:
                if dfs(nei):
                    return True
            state[node]=2
            return False


        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True
            
