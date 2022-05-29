# We need install numpy in order to import it
import numpy as np

# input two matrices
#mat1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3])
#mat2 = ([3, 4, 6],[5, 6, 7],[6,56, 7])

# 11x3 matrix
mat2 = np.array([[1, 0, 0],
                [1, 1, 1],
                [1, 2, 4],
                [1, 3, 9],
                [1, 4, 16],
                [1, 5, 25],
                [1, 6, 36],
                [1, 7, 49],
                [1, 8, 64],
                [1, 9, 81],
                [1, 10, 100]])
# 3x11 matrix
mat1 = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]])

mat3 = np.array([[4], [5], [16], [21], [36], [45],
                [64], [77], [100], [117], [144]])

# This will return dot product
XTX = np.dot(mat1, mat2)


# print resulted matrix
print(XTX)

print()

# inverse matrix
print(np.linalg.inv(XTX))

print()

XTY = np.dot(mat1, mat3)
print(XTY)

print()
print(f"Cramers calculated matrix: \n{np.dot(XTX, XTY)}")
