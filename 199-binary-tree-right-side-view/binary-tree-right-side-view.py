# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rightSideView(self, root):

        if not root:
            return []

        queue = deque([root])
        res = []

        while queue: 

            size = len(queue)
            res.append(queue[size - 1].val)

            for i in range(size):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return res

