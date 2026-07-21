class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        #leftChoices=current_index-i and rightChoices=i=current_index
        MOD=10**9+7
        n=len(arr)
        pse=[-1] *n                  #[-1,-1,-1.....]
        stack=[]
        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if stack:
                pse[i]=stack[-1]
            stack.append(i)
        nse=[n]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                nse[i]=stack[-1]
            stack.append(i)
        ans=0

        for i in range(n):
            l=i-pse[i]
            r=nse[i]-i
            ans=(ans+arr[i]*l*r)%MOD
        return ans

        
        