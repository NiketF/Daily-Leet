# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        index=[0]
        def build(lower,upper):
            if index[0]==len(preorder):
                return None

            value=preorder[index[0]]
            if value<lower or value>upper:
                return None

            node=TreeNode(value)
            index[0]+=1

            node.left=build(lower,value)
            node.right=build(value,upper)

            return node
        return build(float("-inf"),float("inf"))

        