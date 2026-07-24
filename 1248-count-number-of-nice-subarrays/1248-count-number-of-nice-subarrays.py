class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=0
        prefix=0
        freq={0:1}
        for num in nums:
            prefix+=num%2

            if prefix-k in freq:
                ans+=freq[prefix-k]
            freq[prefix]=freq.get(prefix,0)+1
        return ans
        