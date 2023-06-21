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


