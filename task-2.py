import numpy as np
#Slice and print the subarray of the central 3x3 game board.


game_board = np.array([[ 1,  2,  3,  4,  5],
                       [ 6,  7,  8,  9, 10],
                       [11, 12, 13, 14, 15],
                       [16, 17, 18, 19, 20],
                       [21, 22, 23, 24, 25]])

central_slice = game_board[1:4,1:4]
print(central_slice)
