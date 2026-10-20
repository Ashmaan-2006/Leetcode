class Solution(object):
    def isValidSudoku(self, board):
        
        for row in range(len(board)):

            seen = set()

            for col in range(len(board)):

                if board[row][col] == '.':
                    continue

                if board[row][col] in seen:
                    return False
                    
                else:
                    seen.add(board[row][col])


        for col in range(len(board[0])):

            seen = set()

            for row in range(len(board)):

                if board[row][col] == '.':
                    continue

                if board[row][col] in seen:
                    return False
                    
                else:
                    seen.add(board[row][col])


        for i in range(0, 9, 3):
            for j in range(0, 9, 3):

                seen = set()

                for row in range(i, i + 3):
                    for col in range(j, j + 3):

                        if board[row][col] == '.':
                            continue
                        
                        if board[row][col] in seen:
                            return False
                    
                        else:
                            seen.add(board[row][col])


        return True


        

        

                


