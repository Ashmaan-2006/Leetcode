class Solution(object):
    def spiralOrder(self, matrix):

    #    while it exists: 
    #     top 
    #     right
    #     bottom is reversed 
    #     left
    #     repeat

        ret = []

        # matrix = [[5,6,7]]

        while matrix:  #making sure we are only going through it while it exists
            
            if matrix:   #while there are rows in the matrix and the first row got columns, as the first row is going to be used
                
                ret += matrix.pop(0)   #top

            if matrix and matrix[0]:

                for row in matrix:

                    ret.append(row.pop())

            if matrix:

                ret += matrix.pop()[::-1]

            if matrix and matrix[0]:

                for row in matrix[::-1]:

                    ret.append(row.pop(0))

        return ret













        