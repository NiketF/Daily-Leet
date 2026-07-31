class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res=[intervals[0]]
        for start,end in intervals[1:]:
            lastEnd=res[-1][1]
            if start<=lastEnd:
                res[-1][1]=max(lastEnd,end)
            else:
                res.append([start,end])
        return res



        