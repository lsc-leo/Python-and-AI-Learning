'''
rules:
- each row can only contain each digit once
- each column can only contain each digit once
- each 3x3 square can only contain each digit once
'''

board = [[0, 0, 3, 0, 0, 0, 0, 0, 7],
         [4, 2, 0, 0, 9, 1, 0, 0, 0],
         [0, 1, 5, 0, 6, 8, 3, 0, 0],
         [8, 7, 0, 0, 3, 4, 9, 0, 6],
         [3, 0, 0, 0, 0, 0, 0, 5, 1],
         [2, 0, 6, 0, 8, 9, 4, 0, 3],
         [5, 9, 0, 2, 1, 6, 0, 0, 0],
         [1, 0, 2, 9, 0, 7, 0, 8, 0],
         [7, 0, 0, 0, 5, 0, 0, 0, 0]]

#does this print? - yes, but inflexible
#for row in board:
#    print(row)

def normal_board():
    for oInd, row in enumerate(board):
        for iInd, num in enumerate(row):
            print(num, end=" ")
        print()
        
normal_board()


def fancy_board_verions():
    for outerInd, row in enumerate(board):
        for ind, num in enumerate(row):
            print(num, end=" ")
            if (ind+1) % 3 == 0 and ind != 8:
                print("|", end = "")
        print()
        if (outerInd + 1) % 3 == 0 and outerInd != 8:
            print("-------------------") 