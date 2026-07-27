class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=[]
        for i in range(len(nums)):
            for j in range(i):
                prod=(nums[i]-1)*(nums[j]-1)
                m.append(prod)
        return max(m)

        