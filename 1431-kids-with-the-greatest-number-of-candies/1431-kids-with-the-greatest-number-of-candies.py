class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res=[]
        max_c=max(candies) #5
        for i in candies:
            i=i+extraCandies
            if i>=max_c:
                res.append(True)
            else:
                res.append(False)
        return res
            
        

        