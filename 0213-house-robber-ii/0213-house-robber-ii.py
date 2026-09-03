class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        def rob_linear(house):
            prev_one=0
            prev_two=0

            for money in house:
                curr=max(prev_one,prev_two+money)
                prev_two=prev_one
                prev_one=curr
            return prev_one
        return max(
            rob_linear(nums[:-1]), #Not considering last house
            rob_linear(nums[1:]) #Not considering first house
        )
        