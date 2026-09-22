class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask=0xFFFFFFFF
        while b & mask!=0:
            carry=a&b
            a=a^b
            b=carry<<1
        return (a&mask) if (a & 0x80000000)==0 else ~((a^mask)&mask)