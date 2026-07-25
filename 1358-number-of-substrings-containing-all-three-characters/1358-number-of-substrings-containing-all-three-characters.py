class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        count=0
        n=len(s)
        freq={}
        for right in range(n):
            freq[s[right]]=freq.get(s[right],0)+1
            while(freq.get('a',0)>0 and 
            freq.get('b',0)>0 and 
            freq.get('c',0)>0):
                count+=(n-right)
                freq[s[left]]-=1
                left+=1
        return count


"""  #BRUTE FORCE     count=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                sub=s[i:j]
                if 'a' in sub and 'b' in sub and 'c' in sub:
                    count+=1
        return count""" 
        


                

        
                
        