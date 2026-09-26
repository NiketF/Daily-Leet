class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups={}
        for i in strs:
            key=''.join(sorted(i ))
            if key not in groups:
                groups[key]=[]
            groups[key].append(i)
        return list(groups.values())

