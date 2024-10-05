import numpy as np

def recalcMatrix(matrix, solvElement, solvRow, solvColumn):
    newMatrix = np.zeros((len(matrix), len(matrix[0])))

    for j in range(len(matrix[solvRow])):
        newMatrix[solvRow][j] = round(matrix[solvRow][j] / solvElement, 3)

    for i in range(len(matrix)):
        if i == solvRow:
            continue

        for j in range(len(matrix[i])):
            if j == solvColumn:
                continue

            newMatrix[i][j] = round(((matrix[i][j] * solvElement) - (matrix[solvRow][j] * matrix[i][solvColumn])) / solvElement, 3)
    
    return newMatrix
            
def getSolvRow(matrix, solvColumn):
    minSimplix = 999999
    solvRow = -1
    for i in reversed(range(len(matrix) - 1)): # ignore last row
        b = matrix[i][len(matrix[i]) - 1]
        if ((b <= 0 and matrix[i][solvColumn] < 0) or (b >= 0 and matrix[i][solvColumn] > 0)) and (b / matrix[i][solvColumn] <= minSimplix):
            solvRow = i
            minSimplix = b / matrix[i][solvColumn]

    if (solvRow == -1):
        raise Exception("Разрешающая строка не найдена")
    
    return solvRow

def getSolvColumnPossibleSolution(matrix):
    solvColumn = -1
    # i - row
    # j - column
    for i in range(len(matrix) - 1): # ignore last row
        if matrix[i][len(matrix[i]) - 1] > 0:
            continue

        for j in range(len(matrix[i])):
            if matrix[i][j] < 0:
                solvColumn = j
                break
        
        if solvColumn == -1:
            raise Exception("The system of restrictions is contradictory")
        else:
            break

    return solvColumn

def getSolvColumnOptimalSolution(matrix):
    solvColumn = -1
    lastRow = matrix[len(matrix) - 1]

    maxElement = -999999999
    for j in range(len(lastRow) - 1): # ignore last element
        if lastRow[j] < 0 and abs(lastRow[j]) > maxElement:
            maxElement = abs(lastRow[j])
            solvColumn = j
    
    if solvColumn == -1:
        raise Exception("The solution is already optimal")
    
    return solvColumn

def isHasPossibleSolution(matrix):
    for i in range(len(matrix) - 1): # ignore last row
        if matrix[i][len(matrix[i]) - 1] < 0:
            return True
    
    return False

def isHasOptimalSolution(matrix):
    lastRow = matrix[len(matrix) - 1]
    for j in range(len(lastRow) - 1): # ignore last element
        if lastRow[j] < 0:
            return True

    return False

def simplix(matrix):
    newMatrix = matrix  
    iter = 1
    while True:
        if isHasPossibleSolution(newMatrix):
            solvColumn = getSolvColumnPossibleSolution(newMatrix)
        elif isHasOptimalSolution(newMatrix):
            solvColumn = getSolvColumnOptimalSolution(newMatrix)
        else:
            print("!!!!Найдено решение!!!!")
            break

        print("Итерация", iter)

        solvRow = getSolvRow(newMatrix, solvColumn)
        solvElement = newMatrix[solvRow][solvColumn]
        print("Разрешающий столбец:", solvColumn + 1)
        print("Разрешающая строка:", solvRow + 1)
        print("Разрешающий элемент:", solvElement)

        newMatrix = recalcMatrix(newMatrix, solvElement, solvRow, solvColumn)
        print(newMatrix)           

        iter += 1
        print("-----------------")


# simplix([
#     [-5, 1, 1, 1, 0, 3],
#     [2, -2, 1, 0, 1, -6],
#     [4, 4, -4, 0, 0, 0]
# ])

# simplix([
#     [5, -2, 1, 0, 0, 4],
#     [-1, 2, 0, 1, 0, 4],
#     [-1, -1, 0, 0, 1, -4],
#     [3, -6, 0, 0, 0, 0]
# ])

# simplix([
#     [1, 1, 1, 0, 0, 6],
#     [-1, -4, 0, 1, 0, -4],
#     [0, 1, 0, 0, 1, 2],
#     [1, 3, 0, 0, 0, 0]
# ])

# simplix([
#     [1, 2, 1, 0, 0, 0, 6],
#     [2, 1, 0, 1, 0, 0, 8],
#     [-1, 1, 0, 0, 1, 0, 1],
#     [0, 1, 0, 0, 0, 1, 2],
#     [-3, -2, 0, 0, 0, 0, 0]
# ])

# simplix([
#     [0, 1, 2/3, -1/3, 0, 0, 10/3],
#     [1, 0, -1/3, 2/3, 0, 0, 1/3],
#     [0, 0, -1, 1, 1, 0, -2],
#     [0, 0, -2/3, 1/3, 0, 1, -4/3],
#     [0, 0, 1/3, 4/3, 0, 0, 23/3]
# ])

simplix([
    [0, 1, 0, -1, 2, 0, -8, 0, -200],
    [0, 0, 1, 1, 0, 2, 0, 0, 420],
    [1, 0, 0, 1, 0, 0, 8, 0, 480],
    [0, 0, 0, -1, -2, -2, -8, 1, -740],
    [0, 0, 0, 1, 24, 10, 16, 0, 6420]
])