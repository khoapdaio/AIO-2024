import math
import random


def sigmoid( x ):
	"""
    Hàm Sigmoid chuẩn.

    Args:
      x: Giá trị đầu vào.

    Returns:
      Giá trị đầu ra sau khi áp dụng hàm Sigmoid.
    """
	return 1 / (1 + math.exp(-x))


# Hàm chính của chương trình
def main():
	"""
	Hàm này tạo ra một danh sách ngẫu nhiên các số nguyên và áp dụng hàm Sigmoid cho mỗi phần tử trong danh sách.
	"""
	# Tạo một danh sách rỗng để lưu trữ các số ngẫu nhiên
	random_list = []

	# Đặt số lượng số ngẫu nhiên cần tạo
	n = 100

	# Đặt giới hạn dưới và giới hạn trên cho phạm vi số ngẫu nhiên
	l = 0
	r = 1

	# Lặp để tạo danh sách n số ngẫu nhiên
	for _ in range(n):
		# Tạo một số ngẫu nhiên trong khoảng [l, r]
		random_num = random.randint(l, r)
		# Thêm số ngẫu nhiên vào danh sách
		random_list.append(random_num)

	# Sử dụng list comprehension để áp dụng hàm Sigmoid cho mỗi phần tử
	# trong danh sách random_list và tạo danh sách kết quả
	sigmoid_list = [sigmoid(i) for i in random_list]

	# In danh sách kết quả sau khi áp dụng Sigmoid
	print(sigmoid_list)


# Khối này đảm bảo mã chỉ chạy khi tập lệnh được thực thi trực tiếp
if __name__ == '__main__':
	main()
