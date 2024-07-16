import numpy as np

vector_a = np.arange(0, 5)
vector_b = np.arange(10, 15)
matrix_a = np.arange(0, 10).reshape(2, 5)
matrix_b = np.arange(10, 20).reshape(2, 5)
matrix_c = np.arange(0, 8, 2).reshape(2, 2)
print(f"vector_a=>{vector_a}")
print(f"vector_b=>{vector_b}")
print(f"matrix_a=>{matrix_a}")
print(f"matrix_b=>{matrix_b}")
print(f"matrix_c=>{matrix_c}")


# 1) Các phép toán trên vector và ma trận
# a) Đội dài của vector

def compute_vector_length(vector):
	len_of_vector = np.linalg.norm(vector)
	return len_of_vector


print("a) Đội dài của vector")
print(f"vector_a=>{vector_a}")
print(f"compute_vector_length=>{compute_vector_length(vector_a)}")
print(round(compute_vector_length(np.array([-2, 4, 9, 21])), 2))


# b) Phép tích vô hướng

def compute_dot_product(vector1, vector2):
	dot_product = np.dot(vector1, vector2)
	return dot_product

v1 = np. array ([0 , 1 , -1 , 2])
v2 = np. array ([2 , 5 , 1 , 0])
print("b) Phép tích vô hướng")
print(f"vector_a=>{vector_a}")
print(f"vector_b=>{vector_b}")
print(f"compute_dot_product=>{compute_dot_product(vector_a, vector_b)}")
print ( round (compute_dot_product (v1 , v2) ,2) )

# c) Nhân vector với ma trận:
def matrix_multi_vector(matrix, vector):
	result = np.dot(matrix, vector)

	return result


print("c) Nhân vector với ma trận:")
print(f"vector_a=>{vector_a}")
print(f"matrix_a=>{matrix_a}")
print(f"matrix_multi_vector=>{matrix_multi_vector(matrix_a, vector_a)}")


# d) Nhân ma trạn với  ma trận
def matrix_multi_matrix(matrix1, matrix2):
	result = np.multiply(matrix1, matrix2)
	return result


print("d) Nhân ma trạn với  ma trận:")
print(f"matrix_a=>{matrix_a}")
print(f"vector_a=>{matrix_b}")
print(f"matrix_multi_matrix=>{matrix_multi_matrix(matrix_a, matrix_b)}")


# e) Ma trận nghịch đảo

def inverse_matrix(matrix):
	result = np.linalg.inv(matrix)
	return result


print("e) Ma trận nghịch đảo:")
print(f"matrix_c=>{matrix_c}")
print(f"inverse_matrix=>{inverse_matrix(matrix_c)}")
