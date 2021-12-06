def add_file_to_list(filename):
    f = open(filename,"r")
    list = []
    for line in f:
        start=[int(i) for i in line.split()[0].split(',')]
        end=[int(i) for i in line.split()[-1].split(',')]
        list.append([start,end])
    return list

def print_board(board):
    for row in board:
        for x in row:
            print(x,end=' ')
        print('\n', end='')

def run_lines(board,lines):
    for line in lines:
        y1 = line[0][0]; x1 = line[0][1]; y2 = line[1][0]; x2 = line[1][1]
        current_x = x1; current_y = y1
        if x1 == x2:
            while current_y < y2:
                board[current_x][current_y] += 1
                current_y += 1
            while current_y > y2:
                board[current_x][current_y] += 1
                current_y -= 1
            board[x2][y2] += 1
        if y1 == y2:
            while current_x < x2:
                board[current_x][current_y] += 1
                current_x += 1
            while current_x > x2:
                board[current_x][current_y] += 1
                current_x -= 1
            board[x2][y2] += 1
        if abs(x2-x1) == abs(y2-y1):
            while current_x < x2 and current_y < y2:
                board[current_x][current_y] += 1
                current_x += 1; current_y += 1
            while current_x < x2 and current_y > y2:
                board[current_x][current_y] += 1
                current_x += 1; current_y -= 1
            while current_x > x2 and current_y < y2:
                board[current_x][current_y] += 1
                current_x -= 1; current_y += 1
            while current_x > x2 and current_y > y2:
                board[current_x][current_y] += 1
                current_x -= 1; current_y -= 1
            board[x2][y2] += 1
    return board

def count_dangerous_areas(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]>=2:
                count += 1
    return count


dimension = 1000

lines_of_vents = add_file_to_list("input.txt")
board = [[0 for i in range(dimension)] for j in range(dimension)]
board = run_lines(board,lines_of_vents)
#print_board(board)
print(count_dangerous_areas(board))
