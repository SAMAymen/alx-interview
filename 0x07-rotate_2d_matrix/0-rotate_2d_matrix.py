#!/usr/bin/python3
'''2D matrix rotation module'''


def rotate_2d_matrix(matrix):
    '''Rotates a 2D matrix 90° clockwise in place.
    Args:
        matrix (list of list of int): 2D matrix to be rotated.
    Returns:
        None: The matrix is modified in place.
    '''
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # Save the top-left value
            topLeft = matrix[top][left + i]
            # Move the bottom-left value to the top-left position
            matrix[top][left + i] = matrix[bottom - i][left]
            # Move the bottom-right value to the bottom-left position
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # Move the top-right value to the bottom-right position
            matrix[bottom][right - i] = matrix[top + i][right]
            # Move the saved top-left value to the top-right position
            matrix[top + i][right] = topLeft
        right -= 1
        left += 1
