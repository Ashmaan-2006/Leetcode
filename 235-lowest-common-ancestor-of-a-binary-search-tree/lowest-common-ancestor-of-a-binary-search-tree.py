# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        stack = [root]
        parent = {root: None}

        while p not in parent or q not in parent:

            node = stack.pop()

            if node.left:
                stack.append(node.left)
                parent[node.left] = node

            if node.right:
                stack.append(node.right)
                parent[node.right] = node

            
        ancestors = set()

        while p:
            
            ancestors.add(p)

            p = parent[p]

        while q:
            if q in ancestors:
                return q

            q = parent[q]
