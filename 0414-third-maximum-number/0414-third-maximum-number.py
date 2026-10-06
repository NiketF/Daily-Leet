class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first=sec=third=None
        for num in nums:
            if num==first or num==sec or num==third:
                continue
            if first is None or num>first:
                third=sec
                sec=first
                first=num
            elif sec is None or num>sec:
                third=sec
                sec=num
            elif third is None or num>third:
                third=num
        return third if third is not None else first
                
