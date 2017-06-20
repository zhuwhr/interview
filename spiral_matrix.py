'''
spiral matrix problem (aka onion ring problem)
key point is how to control the boundary and handle even/odd size
Some people prefer iterative way, some prefer recursive.
Iterative way looks more intuitive for me.

Invariants:
Given a matrix, print it spirally.
https://leetcode.com/problems/spiral-matrix/#/description

Given a size, generate a spiral matrix
https://leetcode.com/problems/spiral-matrix-ii/#/description

For above two questions, it may also print/generate from either outer to inner or inner to outer

Rotate a sprial matrix
https://leetcode.com/problems/rotate-image/#/submissions/1
'''

def print_spiral(matrix):
    if not matrix or not matrix[0]: return []
    rowStart, rowEnd = 0, len(matrix) - 1
    colStart, colEnd = 0, len(matrix[0]) - 1
    res = []
    
    while rowStart <= rowEnd and colStart <= colEnd:
        # traverse left
        for i in range(colStart, colEnd+1):
            res.append(matrix[rowStart][i])
        rowStart += 1
        # traverse down
        for i in range(rowStart, rowEnd+1):
            res.append(matrix[i][colEnd])
        colEnd -= 1
        # traverse right
        if rowStart <= rowEnd:
            for i in range(colEnd, colStart-1, -1):
                res.append(matrix[rowEnd][i])
            rowEnd -= 1
        # traver up
        if colStart <= colEnd:
            for i in range(rowEnd, rowStart-1, -1):
                res.append(matrix[i][colStart])
            colStart += 1
    return res


def generate_spiral_iter(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    if not n: return []
    n = abs(n)
    rowStart, rowEnd = 0, n-1
    colStart, colEnd = 0, n-1
    num = 1
    res = [[0] * n for _ in range(n)]
    
    while rowStart <= rowEnd and colStart <= colEnd:
        # generate top bound
        for i in range(colStart, colEnd+1):
            res[rowStart][i] = num
            num += 1
        rowStart += 1
        # generate right bound
        for i in range(rowStart, rowEnd+1):
            res[i][colEnd] = num
            num += 1
        colEnd -= 1
        # generate down bound
        if rowStart <= rowEnd:
            for i in range(colEnd, colStart-1, -1):
                res[rowEnd][i] = num
                num += 1
            rowEnd -= 1
        # generate left bound
        if colStart <= colEnd:
            for i in range(rowEnd, rowStart-1, -1):
                res[i][colStart] = num
                num += 1
            colStart += 1
    
    return res


def generate_spiral_recur(n):
    square = [[0] * n for _ in range(n)]
    def generate(square, size, offset, counter):
        if size == 0:
            return square
        if size == 1:
            square[offset][offset] = counter
            return square
        
        # print top row
        for i in range(size - 1):
            square[0 + offset][i + offset] = counter
            counter += 1
        
        # print right col
        for i in range(size - 1):
            square[i + offset][size - 1 + offset] = counter
            counter += 1
        
        # print bottom row
        for i in range(size - 1):
            square[size - 1 + offset][size - 1 + offset - i] = counter
            counter += 1
        
        # print left col
        for i in range(size - 1):
            square[size - 1 + offset - i][0 + offset] = counter
            counter += 1
        
        generate(square, size - 2, offset + 1, counter)
    generate(square, n, 0, 1)
    return square

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    
    for i in range(0, n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(0, n):
        for j in range(0, n // 2):
            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(print_spiral(matrix))

    m = 4
    n = 5
    print(generate_spiral_iter(m))
    print(generate_spiral_iter(n))
    print(generate_spiral_recur(m))
    print(generate_spiral_recur(n))

    mtx = [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]
    rotate(mtx)
    print(mtx)
