import numpy as np

def sudoku():
    return [[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def CheckSpot(puzzle, x, y, n):
    for i in range(9):
        if puzzle[x][i] == n or puzzle[i][y] == n:
            return False

    x0, y0 = (x // 3) * 3, (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if puzzle[x0 + i][y0 + j] == n:
                return False

    return True


def solve(puzzle):
    for x in range(9) :
        for y in range(9):
            if puzzle[x][y] ==0:
                for n in range(1, 10):
                    if CheckSpot(puzzle, x, y, n):
                        puzzle[x][y] = n
                        solve(puzzle)
                        puzzle[x][y] = 0
                return
    print(np.matrix(puzzle))


if __name__ == '__main__':
    puzzle = sudoku()
    # print(np.matrix(puzzle))
    solve(puzzle)
