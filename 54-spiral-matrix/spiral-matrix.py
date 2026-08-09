class Solution(object):
    def spiralOrder(self, matrix):

    #    while it exists: 
    #     top 
    #     right
    #     bottom is reversed 
    #     left
    #     repeat

        ret = []

        while matrix:

            if matrix:

                ret += matrix.pop(0)

            if matrix and matrix[0]:

                for row in matrix:

                    ret.append(row.pop())

            if matrix:

                ret += matrix.pop()[::-1]

            if matrix and matrix[0]:

                for row in matrix[::-1] :
                    ret.append(row.pop(0))

        
        return ret















        