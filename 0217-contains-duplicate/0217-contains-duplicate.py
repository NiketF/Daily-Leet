class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums)!=len(set(nums))
        '''unique=[]
        for i in nums:
            if i in unique:
                return True
            else:
                unique.append(i)
        return False
        65/79 TLE'''

        