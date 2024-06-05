import math
import random


def elu( x, alpha = 1.0 ):
	"""
    Hàm mô phỏng ELU (Exponential Linear Unit) Function.

    Args:
      x: Giá trị đầu vào.
      alpha: Tham số điều chỉnh độ dốc của phần âm. Giá trị mặc định là 1.0.

    Returns:
      Giá trị đầu ra sau khi áp dụng hàm ELU.
    """
	if x >= 0:
		return x
	else:
		return alpha * (math.exp(x) - 1)


# Hàm chính của chương trình
def main():
	"""
	Hàm này tạo ra một danh sách ngẫu nhiên các số nguyên và áp dụng hàm ELU cho mỗi phần tử trong danh sách.
	"""
	# Tạo một danh sách rỗng để lưu trữ các số ngẫu nhiên
	random_list = []

	# Đặt số lượng số ngẫu nhiên cần tạo
	n = 100

	# Đặt giới hạn dưới và giới hạn trên cho phạm vi số ngẫu nhiên
	l = 0
	r = 1

	# Đặt tham số alpha cho hàm ELU
	a = 1.0

	# Tạo số ngẫu nhiên và thêm vào danh sách
	for _ in range(n):
		random_num = random.randint(l, r)
		random_list.append(random_num)

	# Áp dụng hàm ELU cho mỗi phần tử trong danh sách sử dụng list comprehension
	elu_list = [elu(i, a) for i in random_list]

	# In danh sách kết quả sau khi áp dụng ELU
	print(elu_list)


# Khối này đảm bảo mã chỉ chạy khi tập lệnh được thực thi trực tiếp
if __name__ == '__main__':
	main()
