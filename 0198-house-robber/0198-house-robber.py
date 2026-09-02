class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_one=0
        prev_two=0

        for money in nums:
            current=max(prev_one,prev_two+money)
            prev_two=prev_one
            prev_one=current
        return prev_one