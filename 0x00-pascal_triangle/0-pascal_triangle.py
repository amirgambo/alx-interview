#!/usr/bin/python3

'''
A function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n
'''
def pascal_triangle(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        # If so, return an empty list
        return []

   # Initialize an empty list to store the triangle
    triangle = []
    for i in range(n):
        row = [1]

        # Check if this is not the first row (i > 0)
        if i > 0:
            prev_row = triangle[i-1]
            for j in range(1, i):
                row.append(prev_row[j-1] + prev_row[j])
            row.append(1)
        triangle.append(row)

    return triangle
