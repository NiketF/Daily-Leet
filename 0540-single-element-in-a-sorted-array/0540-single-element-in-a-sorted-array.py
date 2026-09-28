class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if mid%2==1:
                mid-=1
            if nums[mid]!=nums[mid+1]:
                right=mid
            else:
                left=mid+2
        return nums[left]



        