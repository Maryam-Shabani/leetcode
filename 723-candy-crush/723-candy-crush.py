class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rsize = len(board)
        csize = len(board[0])
        # def print_board(b):
        #     nonlocal rsize
        #     for ri in range(rsize):
        #         print(b[ri])
        #     print("\n\n")
        is_done = True

        # Scanning Vertically
        for cj in range(csize):
            for ri in range(rsize-2):
                if board[ri][cj] != 0 and abs(board[ri][cj]) == abs(board[ri +1][cj]) == abs(board[ri +2][cj]):
                    board[ri][cj] = board[ri +1][cj] = board[ri +2][cj] = - abs(board[ri][cj])
                    is_done = False

        # Scanning Horisenally
        for ri in range(rsize):
            for cj in range(csize-2):
                if board[ri][cj] != 0 and abs(board[ri][cj]) == abs(board[ri][cj+1]) == abs(board[ri][cj+2]):
                    board[ri][cj] = board[ri][cj+1] = board[ri][cj+2] = - abs(board[ri][cj])
                    is_done = False 

        # Crushing
        if not is_done:
            for cj in range(csize):
                to_be_written_i = -1
                for ri in range(-1, -rsize-1, -1):
                    if board[ri][cj] > 0:
                        board[to_be_written_i][cj] = board[ri][cj]
                        to_be_written_i -=1

                for ri in range(to_be_written_i, -rsize-1 ,-1):
                    board[ri][cj] = 0
        
        return board if is_done else self.candyCrush(board)



            

            


        
        





        