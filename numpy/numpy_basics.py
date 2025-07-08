import numpy as np

matrix1 =np.array([[1,2],[3,4]])
matrix2 =np.array([[5,6],[7,8]])

#sum of matrices

matrix_sum =matrix1 + matrix2;

print("Matrix 1:",matrix1)
print("Matrix 2:",matrix2)
print("Sum of matrices:",matrix_sum)

print("Matrix1 data type:",matrix1.dtype)
print("Matrix1 shape:",matrix1.shape)
print("Matrix_sum shape:",matrix_sum.shape)
print("Matrix_sum dimesnion:",matrix_sum.ndim)

print("Matrix1 itemsize:",matrix1.itemsize)

a =np.arange(5)

print("Array a:",a)

matrix_product = np.dot(matrix1,matrix2)
print("Matrix product:",matrix_product)

#reshaing 
array=np.array([1,2,3,4,5,6])

reshaped_array=array.reshape(3,2)
print("Reshaped array:",reshaped_array)