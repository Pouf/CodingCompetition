def weak_point(matrix):
    rowValues = [sum(row) for row in matrix]
    columnValues = [sum(col) for col in zip(*matrix[::-1])]
    
    minRow = rowValues.index(min(rowValues))
    minCol = columnValues.index(min(columnValues))
    
    return [minRow, minCol]
