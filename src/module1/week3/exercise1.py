import torch
import torch.nn as nn


class Softmax(nn.Module):
	def __init__(self):
		super(Softmax, self).__init__()

	def forward(self, x):
		# Kiểm tra xem đầu vào có phải là tensor 1 chiều hay không
		if x.dim() != 1:
			raise ValueError("Đầu vào phải là một tensor 1 chiều")

		# Tính lũy thừa của từng phần tử trong tensor
		exp_x = torch.exp(x)

		# Chia từng phần tử lũy thừa cho tổng các giá trị lũy thừa để tính softmax
		return exp_x / torch.sum(exp_x)


class SoftmaxStable(nn.Module):
	def __init__(self):
		super(SoftmaxStable, self).__init__()

	def forward(self, x):
		# Kiểm tra xem đầu vào có phải là tensor 1 chiều hay không
		if x.dim() != 1:
			raise ValueError("Đầu vào phải là một tensor 1 chiều")

		# Lấy giá trị lớn nhất trong tensor để trừ đi từng phần tử, giúp tăng độ ổn định tính toán
		max_x = torch.max(x)

		# Tính lũy thừa của từng phần tử sau khi trừ đi giá trị lớn nhất
		exp_x = torch.exp(x - max_x)

		# Chia từng phần tử lũy thừa cho tổng các giá trị lũy thừa để tính softmax
		return exp_x / torch.sum(exp_x)


# Ví dụ sử dụng
x = torch.tensor([1.0, 2.0, 3.0])

# Khởi tạo và sử dụng lớp Softmax
softmax = Softmax()
output = softmax(x)
print("Kết quả Softmax:", output)

# Khởi tạo và sử dụng lớp SoftmaxStable
softmax_stable = SoftmaxStable()
output_stable = softmax_stable(x)
print("Kết quả Softmax ổn định:", output_stable)
