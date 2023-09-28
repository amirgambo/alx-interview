#!/usr/bin/python3

'''
A function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n
'''
def pascal_triangle(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        # If so, return an empty list
        return []

   # Initialize an empty list to store the triangle
    triangle = []
    for i in range(n): # Iterate through each row (i ranges from 0 to n-1)
        row = [1] # Initialize a row with the first element as 1

        # Check if this is not the first row (i > 0)
        if i > 0:
            prev_row = triangle[i-1] # Get the previous row from the triangle
            for j in range(1, i): # Iterate through the elements of the current row (j ranges from 1 to i-1)
                row.append(prev_row[j-1] + prev_row[j]) # Calculate the current element by adding the elements from the previous row
            row.append(1) # Add the last element of the current row, which is always 1
        triangle.append(row) # Add the current row to the triangle

    return triangle # Return the complete Pascal's triangle
