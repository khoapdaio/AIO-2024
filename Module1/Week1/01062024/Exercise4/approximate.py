


def cal_factorial( n ):
	"""
	Hàm này tính giai thừa của một số nguyên không âm.

	Tham số:
		n (int): Số nguyên không âm cần tính giai thừa.

	Trả về:
		int: Giá trị giai thừa của n.

	Ngoại lệ:
		ValueError: Nếu n là số âm.
	"""

	if n < 0:
		raise ValueError("Input phải là số nguyên không âm.")

	if n == 0:
		return 1

	result = 1
	for i in range(1, n + 1):
		result *= i

	return result


def approximate_sin( x, n ):
	"""
	Hàm này tính toán giá trị xấp xỉ của hàm sin(x) sử dụng khai triển Taylor.

	Tham số:
		x (float): Giá trị đầu vào cần tính toán sin(x).
		n (int): Số hạng sử dụng trong khai triển Taylor.

	Trả về:
		float: Giá trị sin(x) xấp xỉ.
	"""

	result = 0
	for i in range(n + 1):
		sign = (-1) ** i
		power = 2 * i + 1
		factorial = cal_factorial(power)
		term = sign * x ** power / factorial
		result += term

	return result


def approximate_cos( x, n ):
	"""
	Hàm này tính toán giá trị xấp xỉ của hàm cos(x) sử dụng khai triển Taylor.

	Tham số:
		x (float): Giá trị đầu vào cần tính toán cos(x).
		n (int): Số hạng sử dụng trong khai triển Taylor.

	Trả về:
		float: Giá trị cos(x) xấp xỉ.
	"""

	result = 1
	for i in range(1, n + 1):
		sign = (-1) ** i
		power = 2 * i
		factorial = cal_factorial(power)
		term = sign * x ** power / factorial
		result += term

	return result


def approximate_sinh( x, n ):
	"""
	Hàm này tính toán giá trị xấp xỉ của hàm sinh(x) sử dụng khai triển Taylor.

	Tham số:
		x (float): Giá trị đầu vào cần tính toán sinh(x).
		n (int): Số hạng sử dụng trong khai triển Taylor.

	Trả về:
		float: Giá trị sinh(x) xấp xỉ.
	"""

	result = 0
	for i in range(n + 1):
		power = 2 * i + 1
		factorial = cal_factorial(power)
		term = x ** power / factorial
		result += term

	return result


def approximate_cosh( x, n ):
	"""
	Hàm này tính toán giá trị xấp xỉ của hàm cosh(x) sử dụng khai triển Taylor.

	Tham số:
		x (float): Giá trị đầu vào cần tính toán cosh(x).
		n (int): Số hạng sử dụng trong khai triển Taylor.

	Trả về:
		float: Giá trị cosh(x) xấp xỉ.
	"""

	result = 1
	for i in range(1, n + 1):
		power = 2 * i
		factorial = cal_factorial(power)
		term = x ** power / factorial
		result += term

	return result
