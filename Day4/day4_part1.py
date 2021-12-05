f = open("input_short.txt","r")
dimension = 5
numbers = []
boards = []
current_board = [[0]*dimension]*dimension
row_in_board = 0
second_row = 1
scores = []

for line in f:
    if len(numbers) == 0:
        numbers = [int(i) for i in line.split(',')]
    elif second_row == 1:
        second_row = 0
    elif line == '\n':
        boards.append(current_board)
        current_board = [[0]*dimension]*dimension
        row_in_board = 0
        scores.append(0)
    else:
        current_board[row_in_board] = [int(i) for i in line.split()]
        row_in_board += 1


