"""Numpy for Economist"""
import numpy as np

array_of_zeros_default = np.zeros(3)

print("array_of_zeros_default:")
print(f"type: {type(array_of_zeros_default)}")
print(f"size: {array_of_zeros_default.size}")
print(f"shape: {array_of_zeros_default.shape}")
print(f"object: {array_of_zeros_default}")

print("array_of_zeros_default[0]:")
print(f"type: {type(array_of_zeros_default[0])}")
print(f"size: {array_of_zeros_default[0].size}")
print(f"size: {array_of_zeros_default[0].shape}")
print(f"object: {array_of_zeros_default[0]}")

array_of_zeros_int = np.zeros(10, dtype=int)

print("array_of_zeros_int:")
print(f"type: {type(array_of_zeros_int)}")
print(f"size: {array_of_zeros_int.size}")
print(f"shape: {array_of_zeros_int.shape}")
print(f"object: {array_of_zeros_int}")

print("array_of_zeros_int[0]:")
print(f"type: {type(array_of_zeros_int[0])}")
print(f"size: {array_of_zeros_int[0].size}")
print(f"shape: {array_of_zeros_int[0].shape}")
print(f"object: {array_of_zeros_int[0]}")

matrix_zeros = np.zeros(4)
matrix_zeros.shape = (2, 2)
print("matrix_zeros:")
print(f"type: {type(matrix_zeros)}")
print(f"size: {matrix_zeros.size}")
print(f"shape: {matrix_zeros.shape}")
print(f"object: {matrix_zeros}")

matrix_identity = np.identity(2)
print("matrix_identity:")
print(f"type: {type(matrix_identity)}")
print(f"size: {matrix_identity.size}")
print(f"shape: {matrix_identity.shape}")
print(f"object: {matrix_identity}")

linspace_array_1_2_5 = np.linspace(start=1, stop=2, num=5)
print("linspace_array_1_2_5:")
print(f"type: {type(linspace_array_1_2_5)}")
print(f"size: {linspace_array_1_2_5.size}")
print(f"shape: {linspace_array_1_2_5.shape}")
print(f"object: {linspace_array_1_2_5}")

print("linspace_array_1_2_5 indexing:")
print(f"linspace_array_1_2_5[0]: {linspace_array_1_2_5[0]}")
print(f"linspace_array_1_2_5[0:2]: {linspace_array_1_2_5[0:2]}")
print(f"linspace_array_1_2_5[-1] (last element): {linspace_array_1_2_5[-1]}")

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("array_2d:")
print(f"type: {type(array_2d)}")
print(f"size: {array_2d.size}")
print(f"shape: {array_2d.shape}")
print(f"object: {array_2d}")

print("array_2d indexing:")
print(f"array_2d[0, 0]: {array_2d[0, 0]}")
print(f"array_2d[0, 1]: {array_2d[0, 1]}")
print(f"array_2d[0, :]: {array_2d[0, :]}")
print(f"array_2d[:, 1]: {array_2d[:, 1]}")

integer_indices = np.array((0, 2, 3))
print("extract elements with arrays of integers:")
print("linspace_array_1_2_5[integer_indices]:", linspace_array_1_2_5[integer_indices])

boolean_indices = np.array([0, 1, 1, 0, 0], dtype=bool)
print("extract elements with arrays of booleans:")
print("linspace_array_1_2_5[boolean_indices]:", linspace_array_1_2_5[boolean_indices])

print("mutate elements:")
print("original array_2d:", array_2d)
array_2d[0, 0] = 0
print("modified array_2d:", array_2d)
array_2d[0, :] = 0
print("modified array_2d:", array_2d)
array_2d[:, 1] = 0
print("modified array_2d:", array_2d)

print("Array Methods:")
print("sort:", linspace_array_1_2_5.sort())
print("sum:", linspace_array_1_2_5.sum())
print("mean:", linspace_array_1_2_5.mean())
print("max:", linspace_array_1_2_5.max())
print("min:", linspace_array_1_2_5.min())
print("argmax:", linspace_array_1_2_5.argmax())
print("argmin:", linspace_array_1_2_5.argmin())
print("std:", linspace_array_1_2_5.std())
print("var:", linspace_array_1_2_5.var())
print("cumsum:", linspace_array_1_2_5.cumsum())
print("cumprod:", linspace_array_1_2_5.cumprod())

print("Arithmetic Operations:")
array_1 = np.array([1, 2, 3, 4])
array_2 = np.array([5, 6, 7, 8])
print("sum:", array_1 + array_2)
print("add scalar:", array_1 + 5)
print("multiply by scalar:", array_1 * 5)
print("difference:", array_1 - array_2)
print("product:", array_1 * array_2)
print("quotient:", array_1 / array_2)
print("remainder:", array_1 % array_2)

print("Matrix Operations:")
matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])
print("matrix_1 + matrix_2:", matrix_1 + matrix_2)
print("matrix_1 * matrix_2:", matrix_1 * matrix_2)
print("matrix_1 / matrix_2:", matrix_1 / matrix_2)
print("matrix_1 @ matrix_2:", matrix_1 @ matrix_2) # inner product

print("linalg Operations:")
print("solve linear matrix equations:", np.linalg.solve(matrix_1, matrix_2))
print("matrix_1 inverse:", np.linalg.inv(matrix_1))
print("matrix_2 inverse:", np.linalg.inv(matrix_2))
print("matrix_1 determinant:", np.linalg.det(matrix_1))
print("matrix_2 determinant:", np.linalg.det(matrix_2))
