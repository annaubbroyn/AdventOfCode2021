def markNumbersAtBoard(board, number):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == number:
                board[i][j] = 'x'
    return board
                
def checkBingo(board):
    #checking bingo on rows
    for i in range(len(board)):
        bingo_row = True
        for j in range(len(board[0])):
            if board[i][j] != 'x':
                bingo_row = False
        if bingo_row == True:
            return True

    #checking bingo on columns
    for j in range(len(board)):
        bingo_col = True
        for i in range(len(board[0])):
            if board[i][j] != 'x':
                bingo_col = False
        if bingo_col == True:
            return True
    
    #returning false if not bingo
    return False

def runBingo(numbers,boards):
    last_board = -1
    boards_left = [i for i in range(len(boards))]
    for number in numbers:
        for i in range(len(boards)):
            boards[i] = markNumbersAtBoard(boards[i],number)
            if checkBingo(boards[i])==True:
                for x in boards_left:
                    if x == i:
                        boards_left.remove(x)
        if len(boards_left) == 1:
            last_board = boards_left[0]
        elif len(boards_left) == 0:
            return [last_board,int(number)]
    return [-1,-1]

def calculateScore(board,last_number):
    sum_ = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]!='x':
                sum_ += int(board[i][j])
    result = sum_*last_number
    return result

f = open("input.txt","r")
dimension = 5
numbers = []
boards = []
current_board = [[0]*dimension]*dimension
row_in_board = 0
second_row = 1

for line in f:
    if len(numbers) == 0:
        numbers = line.split(',')
    elif second_row == 1:
        second_row = 0
    elif line == '\n':
        boards.append(current_board)
        current_board = [[0]*dimension]*dimension
        row_in_board = 0
    else:
        current_board[row_in_board] = line.split()
        row_in_board += 1
boards.append(current_board)

result = runBingo(numbers,boards)
winning_board = boards[result[0]]
last_number = result[1]
print(calculateScore(winning_board,last_number))

