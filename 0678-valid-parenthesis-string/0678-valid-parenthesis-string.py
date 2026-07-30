class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftMin=0
        leftMax=0
        for ch in s:
            if ch=='(':
                leftMin+=1
                leftMax+=1
            elif ch==')':
                leftMin-=1
                leftMax-=1
            else:
                leftMin-=1
                leftMax+=1
            if leftMax<0:
                return False
            elif leftMin<0:
                leftMin=0
        if leftMin==0:
            return True
        return False
            
        