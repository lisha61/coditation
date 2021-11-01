import numpy as np
import sys
import getopt

argv = sys.argv[1:]
opts, args = getopt.getopt(argv, "r:c:p:")
arguments = dict(opts)

for arg in ['-r', '-c', '-p']:
    if arg not in arguments.keys():
        print(f"{arg} is required.")
        exit()


R = int(arguments['-r'])
C = int(arguments['-c'])
P = int(arguments['-p'])


chance = True
condition = False
board = np.zeros((R, C))


def won(b, p):

    for r in range(R):
        for c in range(C - (P - 1)):
            if np.all(b[r][c:c+P] == p):
                return True

    for r in range(R - (P - 1)):
        for c in range(C):
            if np.all(b[r:r+P, c] == p):
                return True

    for r in range(R - (P - 1)):
        for c in range(C - (P - 1)):

            if np.all(b[r:r+P, c:c+P].diagonal() == p):
                return True

            if np.all(np.fliplr(b[r:r+P, c:c+P]).diagonal() == p):
                return True


print(np.flip(board, axis=0))


while not condition:

    if chance == True:
        col = (
            int(input(f"\n\nPlayer 1 (1-{C}): ")) - 1)

        if board[R - 1][col] == 0:
            row = -1
            for r in range(R):
                if board[r][col] == 0:
                    row = r
                    break

            board[row][col] = 1

            if won(board, 1):

                print(np.flip(board, axis=0))
                print("Player 1 won the game.")
                exit()

    else:
        col = (
            int(input(f"\n\nPlayer 2 (1-{C}): ")) - 1)

        if board[R - 1][col] == 0:
            row = -1
            for r in range(R):
                if board[r][col] == 0:
                    row = r
                    break

            board[row][col] = 2

            if won(board, 2):

                print(np.flip(board, axis=0))
                print("Player 2 won the game.")
                exit()

    print(np.flip(board, axis=0))

    if chance == True:
        chance = False
    else:
        chance = True
