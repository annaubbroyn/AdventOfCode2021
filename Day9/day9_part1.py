
def file_to_matrix(filename):
    matrix = []
    f = open(filename,"r")
    for line in f:
        row = []
        [row.append(int(line[i])) for i in range(len(line)-1)]
        matrix.append(row)
    return matrix

def find_lowpoints(hightmap):
    lowpoints = []
    hight = len(hightmap)
    width  = len(hightmap[0])
    for i in range(hight):
        for j in range(width):
            if i == 0 and j == 0:
                if hightmap[1][0]>hightmap[0][0] and hightmap[0][1]>hightmap[0][0]:
                    lowpoints.append(hightmap[0][0])
            elif i == 0 and j == width-1:
                if hightmap[0][width-2]>hightmap[0][width-1] and hightmap[1][width-1]>hightmap[0][width-1]:
                    lowpoints.append(hightmap[0][width-1])
            elif i == hight-1 and j == 0:
                if hightmap[hight-2][0]>hightmap[hight-1][0] and hightmap[hight-1][1]>hightmap[hight-1][0]:
                    lowpoints.append(hightmap[hight-1][0])
            elif i == hight-1 and j == width-1:
                if hightmap[hight-2][width-1]>hightmap[hight-1][width-1] and hightmap[hight-1][width-2]>hightmap[hight-1][width-1]:
                    lowpoints.append(hightmap[hight-1][width-1])
            elif i == 0:
                if hightmap[0][j-1]>hightmap[0][j] and hightmap[0][j+1]>hightmap[0][j] and hightmap[1][j]>hightmap[0][j]:
                    lowpoints.append(hightmap[0][j])
            elif i == hight-1:
                if hightmap[hight-1][j-1]>hightmap[hight-1][j] and hightmap[hight-1][j+1]>hightmap[hight-1][j] and hightmap[hight-2][j]>hightmap[hight-1][j]:
                    lowpoints.append(hightmap[hight-1][j])
            elif j == 0:
                if hightmap[i-1][0]>hightmap[i][0] and hightmap[i+1][0]>hightmap[i][0] and hightmap[i][1]>hightmap[i][0]:
                    lowpoints.append(hightmap[i][0])
            elif j == width-1:
                if hightmap[i-1][width-1]>hightmap[i][width-1] and hightmap[i+1][width-1]>hightmap[i][width-1] and hightmap[i][width-2]>hightmap[i][width-1]:
                    lowpoints.append(hightmap[i][width-1])
            else:
                if hightmap[i-1][j]>hightmap[i][j] and hightmap[i+1][j]>hightmap[i][j] and hightmap[i][j-1]>hightmap[i][j]and hightmap[i][j+1]>hightmap[i][j]:
                    lowpoints.append(hightmap[i][j])
    return(lowpoints)


hightmap = file_to_matrix("input.txt")
lowpoints = find_lowpoints(hightmap)
sum = 0
for x in lowpoints:
    sum += x + 1

print(sum)
