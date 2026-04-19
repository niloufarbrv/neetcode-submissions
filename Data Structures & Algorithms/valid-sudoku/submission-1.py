class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # ["1","2",".",".","3",".",".",".","."],
        # columns [0,1,2] , rows [0,1,2]
        # columns [0,1,2], rows [3,4,5]
        row_num, column_num = 9,9
        for i in range(column_num): #i=0
            column_set = set()
            for j in range(row_num):
                if board[j][i] == ".":
                    continue
                if board[j][i] in column_set:
                    return False
                else:
                    column_set.add(board[j][i])
        
        for j in range(row_num):
            row_set=  set()
            for i in range(column_num):
                if board[j][i] == ".":
                    continue
                if board[j][i] in row_set:
                    return False
                else:
                    row_set.add(board[j][i])
        max_square_rows, max_square_columns  = 2, 2
        
        for j in range(max_square_rows+1):
            # rows ro consider j*3 +(0,1,2)
            for i in range(max_square_columns+1):
                #columns to consider i*3 +(0,1,2)
                rows = [j*3,j*3+1,j*3+2 ]
                columns = [i*3,i*3+1, i*3+2 ]
                three_by_three_set = set()
                for row in rows:
                    for column in columns:
                        if board[row][column] == ".":
                            continue
                        if board[row][column] in three_by_three_set:
                            return False
                        else:
                            three_by_three_set.add(board[row][column])
        
        return True








