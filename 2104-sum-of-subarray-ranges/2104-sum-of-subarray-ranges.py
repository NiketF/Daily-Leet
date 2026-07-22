class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        n=len(nums)
        for i in range(n):
            currMax=nums[i]
            currMin=nums[i]
            for j in range(i,n):
                currMax=max(currMax,nums[j])
                currMin=min(currMin,nums[j])
                ans+=currMax-currMin # To remove the iteration of every stored subarray
        return ans
        

        