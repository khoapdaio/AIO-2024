import numpy as np

# 3) Cosine Similarity
"""
Cosine Similarity (Độ tương đồng cosine ) là một thước đo dùng để xác định độ tương đồng giữa hai vector trong không gian
vector trong không gian vector.

Định nghĩa:
Cosine similarity giữa hai vector A và B được định nghĩa như sau:

Cosine Similarity(A,B)= tích vô hướng / tích độ dài 

"""

vector_3d_A = np.arange(1, 10).reshape(3, 3)
vector_3d_B = np.arange(11, 20).reshape(3, 3)

vector_1d_A = np.arange(1, 5)
vector_1d_B = np.array([1, 0, 3, 0])


def compute_cosine(A, B):
	dot_prod = np.dot(A, B)
	normA = np.linalg.norm(A)
	normB = np.linalg.norm(B)

	cos_sim = dot_prod / (normA * normB)
	return cos_sim


print(f"vector_3d_A: {vector_3d_A}")
print(f"vector_3d_B: {vector_3d_B}")
print(f"cosine similarity: {compute_cosine(vector_3d_A, vector_3d_B)}")

print(f"vector_1d_A: {vector_1d_A}")
print(f"vector_1d_B: {vector_1d_B}")
print(f"cosine similarity: {compute_cosine(vector_1d_A, vector_1d_B)}")
