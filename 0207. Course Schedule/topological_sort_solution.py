class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {i:0 for i in range(numCourses)}
        adj = {i:[] for i in range(numCourses)}

        # instantiate indegree and adjacency graph
        for c, p in prerequisites:
            indegree[c] += 1
            adj[p].append(c)
        
        # add all courses without prereqs in the queue
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        # keep track of the number of nodes visited
        visited = 0
        while queue:
            node = queue.pop(0)
            visited += 1
            # since this course can be taken, we subtract 1 from each of the courses that depend on it, if said course's indegree is now 0, we can also take said course, so append it to queue
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        # check if all courses are visited
        return visited == numCourses