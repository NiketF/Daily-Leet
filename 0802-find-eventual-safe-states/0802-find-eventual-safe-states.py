class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n=len(graph)
        state=[0]*n

        def dfs(node):
            if state[node]==1:
                return False
            if state[node]==2:
                return True
            state[node]=1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node]=2
            return True
        safe=[]
        for node in range(n):
            if dfs(node):
                safe.append(node)
        return safe
        


            

