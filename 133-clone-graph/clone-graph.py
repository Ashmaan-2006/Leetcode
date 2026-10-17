"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):

        clone = {}

        if not node:
            return None

        clone[node] = Node(node.val)
        
        queue = deque([node])

        while queue: 

            temp = queue.popleft()
                
            clone_temp = clone[temp]

            for neighbor in temp.neighbors:

                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                clone_temp.neighbors.append(clone[neighbor])

        return clone[node]



                





            
                