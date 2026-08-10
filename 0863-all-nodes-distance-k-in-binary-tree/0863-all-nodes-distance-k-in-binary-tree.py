# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if not root:
            return []
        parent={}
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if node.left:
                parent[node.left]=node
                queue.append(node.left)
            if node.right:
                parent[node.right]=node
                queue.append(node.right)
        #BFS from target
        queue=deque([target])
        visited=set([target])
        dist=0
        while queue:
            #all nodes in queue
            #exactly K distance away
            if dist==k:
                return [node.val for node in queue]
            for _ in range(len(queue)):
                node=queue.popleft()
                #Move left
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                
                #Move right
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                
                #Move to parent
                if node in parent and parent[node] not in visited:
                    visited.add(parent[node])
                    queue.append(parent[node])
            dist+=1
        return []