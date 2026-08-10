# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        queue=deque([(root,0)])
        max_width=0
        while queue:
            lvl=len(queue)
            first_i=queue[0][1]
            for _ in range(lvl):
                node,index=queue.popleft()
                if node.left:
                    queue.append((node.left,2*index+1))
                if node.right:
                    queue.append((node.right,2*index+2))
            last_i=index
            width=last_i-first_i+1
            max_width=max(max_width,width)
        return max_width

        