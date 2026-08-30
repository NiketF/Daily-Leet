class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        l=0
        r=0

        for i in range(1,n):
            if nums[i] < nums[l]:
                l=i
            
            if nums[i]>nums[r]:
                r=i
        
        if l<r:
            l,r=r,l
        ans=n

        for i in range(n+1):
            e=0

            if r>=i:
                e=n-r
            elif l>=i:
                e=n-l
            ans=min(ans,i+e)
        
        return ans
        