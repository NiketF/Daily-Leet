# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_i={}
        for i in range(len(inorder)):
            inorder_i[inorder[i]]=i
        post_idx=[len(postorder)-1]
        def build(left,right):
            if left>right:
                return None
            root_val=postorder[post_idx[0]]
            post_idx[0]-=1
            root=TreeNode(root_val)
            mid=inorder_i[root_val]
            root.right=build(mid+1,right)
            root.left=build(left,mid-1)
            return root
        return build(0,len(inorder)-1)

        
        