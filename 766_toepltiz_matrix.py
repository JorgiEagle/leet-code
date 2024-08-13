def isToeplitzMatrix(matrix: list[list[int]]) -> bool:
    for x in range(len(matrix[0])):
        element = matrix[0][x]
        for j in range(len(matrix)-x):
            comp = matrix[j][(j+x)%len(matrix[0])]
            if element != comp:
                return False
    for y in range(1, len(matrix)):
        element = matrix[y][0]
        for k in range(len(matrix)-y):
            comp = matrix[k][(y+k)%len(matrix)]
            if element != comp:
                return False
    return True

isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])