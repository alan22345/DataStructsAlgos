import math

# sudoku checker

def sudokuChecker(sudoku):
    
    def hasDuplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))
    
    n = len(sudoku)

    if any(
        hasDuplicate(sudoku[i][j] for j in range(n))
        or hasDuplicate(sudoku[j][i] for j in range(n))
        for i in range(n)):
            return False
    
    regionSize = int(math.sqrt(n))
    return all(not hasDuplicate([
        sudoku[a][b]
        for a in range(regionSize * I, regionSize *(I + 1))
        for b in range(regionSize * J, regionSize * (J + 1))
    ]) for I in range(regionSize) for J in range(regionSize))


# compute spiral ordering of a 2D array
# return the spiral ordering of the array 

def matrixInSpiralOrder(squareMatrix):

    def matrixLayerInClockwise(offset):
        if offset == len(squareMatrix) - offset - 1:
            spiralOrdering.append(squareMatrix[offset][offset])
            return
        spiralOrdering.extend(squareMatrix[offset][offset:-1 - offset])
        spiralOrdering.extend(
            list(zip(*squareMatrix))[-1 - offset][offset:-1 - offset])
        spiralOrdering.extend(
            squareMatrix[-1 - offset][-1 -offset:offset:-1])
        spiralOrdering.extend(list(zip(*squareMatrix))[offset][-1-offset:offset:-1])
    
    spiralOrdering = []

    for offset in range((len(squareMatrix)+1)//2):
        matrixLayerInClockwise(offset)
    return spiralOrdering

def matrixInSpiralOrder2(squareMatrix):
    SHIFT = ((0,1),(1,0),(0,-1),(-1,0))
    direction = x = y = 0
    spiralOrdering = []

    for _ in range(len(squareMatrix)**2):
        spiralOrdering.append(squareMatrix[x][y])
        squareMatrix[x][y] = 0
        nextX, nextY = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (nextX not in range(len(squareMatrix))
            or (nextY not in range(len(squareMatrix)))
            or squareMatrix[nextX][nextY] == 0):
            direction = (direction + 1) & 3
            nextX, nextY = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x,y = nextX,nextY
    return spiralOrdering
 
snail = [[1,2,3],
         [4,5,6],
         [7,8,9]]
# print(matrixInSpiralOrder2(snail))

# rotate a 2D array by 90 degrees

def rotateMatrix(squareMatrix):
    matrixSize = len(squareMatrix) - 1
    for i in range(len(squareMatrix) // 2):
        for j in range(i, matrixSize - j):
            (squareMatrix[i][j], squareMatrix[~j][i], squareMatrix[~i][~j],
            squareMatrix[~j][i]) = (squareMatrix[~j][i], squareMatrix[~i][~j]
            , squareMatrix[j][~i],squareMatrix[i][j])

# rows in pascals triangle
# given a number n return first n rows of pascals triangle

def pascalsTriangle(n):
    result = [[1]*(i+1) for i in range(n)]
    for i in range(n):
        for j in range(1,i):
            result[i][j] = result[i-1][j-1] + result[i-1][j]
    return result

print(pascalsTriangle(5))