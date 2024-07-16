# 2) Eigenvector và eigenvalues
import numpy as np

vector = np.array([[0.9, 0.2], [0.1, 0.8]])


"""
Eigenvectors và eigenvalues là các khái niểm quan trọng trong đại số tuyến tính và được sử dụng rộng rãi trong nhiều
lĩnh vực khoa học máy tính, vật lý, kinh tế và thống kê

Định nghĩa:
- Eigenvector (vector riêng ) của một ma trận vuông A là một vector không đổi hướng khi được biến đổi bởi ma trận A.
Nói cách khác, nếu v là một eigenvector của A, thì:
trong đó, λ là một số vô hướng gjoji là eigenvalue (giá trị riêng ) tương ứng với eigenvector v 

- Eigenvalue (giá trị riêng) λ của một ma trận vuông A là một số vô hướng sao cho tồn tại một eigenvector v thỏa mãn 
phương trình trên

Các bước thực hiện
- input: một ma trận vuông
- output: Eigenvector, Eigenvalue

* b1: Tính Eigenvalue bằng công thức đặc trưng
det(A−λI)=0

trong đó:
A là vector đầu vào cần tìm Eigenvectors và eigenvalues
I là vector ma trận đơn vị có cùng kích thước bằng với vector A
λ là Eigenvalue giá trị cần tính từ công thức trên


* b2: 
Tương ứng với mỗi eigenvalue, ta sẽ tìm eigenvector bằng công thức sau
(A − λI)v = 0
"""

def compute_eigenvalues_eigenvectors(matrix):
	return np.linalg.eig(matrix)


print(f"vector=>{vector}")
print(f"compute_eigenvalues_eigenvectors=>{compute_eigenvalues_eigenvectors(vector)}")
