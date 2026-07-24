class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        ans=0
        prefix=0
        freq={0:1}
        for num in nums:
            prefix+=num

            if prefix-goal in freq:
                ans+=freq[prefix-goal]
            freq[prefix]=freq.get(prefix,0)+1
        return ans


        