class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums1)):
            idx=nums2.index(nums1[i])
            found=False
            for j in range(idx+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    ans.append(nums2[j])
                    found=True
                    break
            if found==False:
                ans.append(-1)
        return ans


        

        