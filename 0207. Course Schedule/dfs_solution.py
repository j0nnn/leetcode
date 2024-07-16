class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        # instantiate adjacency graph
        for c, p in prerequisites:
            adj[c].append(p)

        # visited set to track for cycles
        visited = set()

        # dfs function that traverses upwards to see if all of its prereqs can be taken 
        def dfs(node):
            # cycle detection, return false
            if node in visited: return False
            # course has no prereqs, return true
            if len(adj[node]) == 0: return True

            visited.add(node)

            # perform dfs on its prereqs return false if any of its prereqs cannot be taken
            for p in adj[node]:
                if not dfs(p):
                    return False
            visited.remove(node)
            return True
        
        # perform dfs on all possible courses to ensure every course can be taken
        for i in range(numCourses):
            if not dfs(i):
                return False
            # if a course can be taken, set its prereq to empty list to avoid recomputation for future calculations
            adj[i] = []
        return True
