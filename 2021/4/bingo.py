
import re
import copy

class Board:

    def __init__(self, lines):
        self.rows = []
        for line in lines:
            self.rows.append([int(num) for num in line.strip().split(' ')])
        self.cols = []
        for i in range(len(self.rows[0]) ):
            self.cols.append([ r[i] for r in self.rows])

    def checkNum(self,  num: int ):
        found = False
        for row in self.rows:
            if num in row:
                row[ row.index(num) ] = -1
                found = True
        if found:
            for col in self.cols:
                if num in col:
                    col[ col.index(num) ] = -1

    def checkWin(self):
        rowWins = [sum(row)==-5 for row in self.rows]
        colWins = [sum(col)==-5 for col in self.cols]
        return sum(rowWins) + sum(colWins) > 0

    def printBoard(self):
        for row in self.rows:
            for num in row:
                if num == -1: print(' X ', end='')
                else: print(f'{num:02} ', end='')
            print()

boards = []
selections = []
with open('bingo.txt', 'r') as bingo:

    selections = [int(num) for num in bingo.readline().strip().split(',')]
    lines = []
    for line in bingo.readlines():
        if len(line.strip()) == 0:
            if len(lines) == 5:
                boards.append(Board(lines))
            lines = []
        else:
            lines.append(re.sub('\s+',' ',line))

blank_boards = copy.deepcopy(boards)

winNum = 0
winBoard = 0
for i, num in enumerate(selections):
    winner = False
    for board in boards:
        board.checkNum(num)
        if board.checkWin():
            winner = True
            winBoard = board
            break
    if winner:
        winNum = i
        break

print('Part one:\n')
winSum = 0
print(f'Selections: {" ".join([str(num) for num in selections[:winNum+1]])}')
for row in winBoard.rows:
    for num in row:
        if num >= 0: winSum += num
print('\nWinning board: ')
winBoard.printBoard()
print(f'\nWinning num = {selections[winNum]}, board sum = {winSum}, product = {selections[winNum]*winSum}')

boards.remove(winBoard)

winNum = 0
winBoard = 0
winningBoards = 0
removeBoards = []
for i, num in enumerate(selections):
    for board in blank_boards:
        board.checkNum(num)
        if board.checkWin():
            winningBoards += 1
            winBoard = board
            winNum = i
            removeBoards.append(board)
    for board in removeBoards:
        blank_boards.remove(board)
    removeBoards = []

print('Part two:\n')
winSum = 0
print(f'Selections: {" ".join([str(num) for num in selections[:winNum+1]])}')
for row in winBoard.rows:
    for num in row:
        if num >= 0: winSum += num
print('\nLast winning board: ')
winBoard.printBoard()
print(f'\nWinning num = {selections[winNum]}, board sum = {winSum}, product = {selections[winNum]*winSum}')