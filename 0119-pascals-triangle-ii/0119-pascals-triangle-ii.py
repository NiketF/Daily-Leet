class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row=[1]
        for i in range(rowIndex):
            next_val=row[-1]*(rowIndex-i)//(i+1)
            row.append(next_val)
        return row
