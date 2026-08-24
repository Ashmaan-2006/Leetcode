class Solution(object):
    def spiralOrder(self, matrix):

        output = []
        
        while matrix:

            if matrix and matrix[0]:

                output += matrix.pop(0)

            if matrix and matrix[0]:

                for num in matrix:
                    output.append(num.pop())

            if matrix:

                output += matrix.pop()[::-1]

            if matrix and matrix[0]:

                for num in matrix[::-1]:

                    output.append(num.pop(0))

        return output
                



        