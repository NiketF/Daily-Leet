class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        visited=[False]*n
        count=0

        def dfs(city):
            visited[city]=True

            for neighbour in range(n):
                if isConnected[city][neighbour]==1 and not visited[neighbour]:
                    dfs(neighbour)
        
        for city in range(n):
            if not visited[city]:
                count+=1
                dfs(city)
        return count