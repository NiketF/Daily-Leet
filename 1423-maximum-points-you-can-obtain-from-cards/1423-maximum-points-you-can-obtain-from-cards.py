class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        total=sum(cardPoints[len(cardPoints)-k:])
        res=total
        for right in range(len(cardPoints)-k,len(cardPoints)):
            total+=cardPoints[left]-cardPoints[right]
            res=max(res,total)
            left+=1
        return res


        