# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        else:
            #No left child
            if root.left is None:
                return root.right
            #No right child
            if root.right is None:
                return root.left
            
            #Node has 2 childs, pick the smallest one and replace it with root
            successor=root.right
            while successor.left is not None:
                successor=successor.left
            root.val=successor.val
            root.right=self.deleteNode(root.right,successor.val)
        return root