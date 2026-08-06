class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            temp=n
            prod=1
            while temp>0:
                prod*=temp%10
                temp//=10
            if prod%t==0:
                return n
            n+=1





        