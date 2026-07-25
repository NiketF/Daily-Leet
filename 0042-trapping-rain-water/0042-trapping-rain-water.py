class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftMax=[0]*len(height)
        rightMax=[0]*len(height)
        leftMax[0]=height[0]
        rightMax[-1]=height[-1]
        water=0
        for i in range(1,len(height)):
            leftMax[i]=max(leftMax[i-1],height[i])
        for j in range(len(height)-2,-1,-1):
            rightMax[j]=max(rightMax[j+1],height[j])
        for k in range(len(height)):
            water+=min(leftMax[k],rightMax[k])-height[k]
        return water
    


        