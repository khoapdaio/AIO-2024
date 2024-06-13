import random


def relu( x ):
	"""
    Hàm mô phỏng ReLU Function.

    Args:
      x: Giá trị đầu vào.

    Returns:
      Giá trị đầu ra sau khi áp dụng hàm ReLU.
    """
	return max(0, x)


def main():
	random_list = []
	n = 100
	l = 0
	r = 1
	for _ in range(n):
		random_num = random.randint(l, r)
		random_list.append(random_num)
	print([relu(i) for i in random_list])


if __name__ == '__main__':
	main()
