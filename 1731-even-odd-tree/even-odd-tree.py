class Solution(object):
    def isEvenOddTree(self, root):

        if not root:
            return False

        queue = deque([root])
        count = 0

        while queue:

            size = len(queue)

            if count % 2 == 0:
                for i in range(size):
                    if i == 0:
                        if queue[i].val % 2 == 0:
                            return False
                    else:
                        if queue[i].val <= queue[i - 1].val:
                            return False
                        if queue[i].val % 2 == 0:
                            return False

            else:
                for i in range(size):
                    if i == 0:
                        if queue[i].val % 2 != 0:
                            return False
                    else:
                        if queue[i].val >= queue[i - 1].val:
                            return False
                        if queue[i].val % 2 != 0:
                            return False

            for i in range(size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            count += 1

        return True