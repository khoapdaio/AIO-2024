import math
import random
import unittest

from src.module1.week1.exercise1 import evaluate_classification
from src.module1.week1.exercise2 import elu, relu, sigmoid
from src.module1.week1.exercise4.approximate import cal_factorial, approximate_sin, approximate_cos, approximate_sinh, \
	approximate_cosh
from src.module1.week1.exercise5.mean_different import calculate_mdnre


class TestWeek1(unittest.TestCase):

	def test_evaluate_classification(self):
		tp = 123
		fp = 'a'
		fn = 123

		# Call the evaluation function with the calculated values
		self.assertIsNone(evaluate_classification(tp = tp, fp = fp, fn = fn))
		tp = 123
		fp = 123
		fn = 'a'

		self.assertIsNone(evaluate_classification(tp = tp, fp = fp, fn = fn))
		tp = 'a'
		fp = 123
		fn = 123
		self.assertIsNone(evaluate_classification(tp = tp, fp = fp, fn = fn))

		tp = 123
		fp = 123
		fn = 123
		self.assertIsNone(evaluate_classification(tp = tp, fp = fp, fn = fn))

		tp = 0
		fp = 0
		fn = 0
		self.assertIsNone(evaluate_classification(tp = tp, fp = fp, fn = fn))

	def test_elu(self):
		"""
			Hàm này tạo ra một danh sách ngẫu nhiên các số nguyên và áp dụng hàm ELU cho mỗi phần tử trong danh sách.
			"""
		# Tạo một danh sách rỗng để lưu trữ các số ngẫu nhiên
		random_list = []

		# Đặt giới hạn dưới và giới hạn trên cho phạm vi số ngẫu nhiên
		l = -1
		r = 1

		# Đặt tham số alpha cho hàm ELU
		a = 1.0

		# Tạo số ngẫu nhiên và thêm vào danh sách

		random_list.append(random.randint(-1, 1))
		random_list.append(random.randint(-1, 1))
		random_list.append(random.randint(-1, 1))
		random_list.append(random.randint(-1, 1))
		random_list.append(random.randint(-1, 1))
		random_list.append(random.randint(-1, 1))

		# Áp dụng hàm ELU cho mỗi phần tử trong danh sách sử dụng list comprehension
		elu_list = [elu(i, a) for i in random_list]

		# In danh sách kết quả sau khi áp dụng ELU
		print(elu_list)

	def test_relu(self):
		random_list = []

		random_list.append(random.randint(0, 1))
		random_list.append(random.randint(0, 1))
		random_list.append(random.randint(0, 1))
		random_list.append(random.randint(0, 1))
		random_list.append(random.randint(0, 1))
		random_list.append(random.randint(0, 1))
		print([relu(i) for i in random_list])

	def test_sigmoid(self):
		# Tạo một danh sách rỗng để lưu trữ các số ngẫu nhiên
		random_list = []

		# Thêm số ngẫu nhiên vào danh sách
		random_list.append(random.randint(0, 1))
		random_list.append(random.randint(0, 1))
		random_list.append(random.randint(0, 1))
		random_list.append(random.randint(0, 1))
		random_list.append(random.randint(0, 1))

		# Sử dụng list comprehension để áp dụng hàm Sigmoid cho mỗi phần tử
		# trong danh sách random_list và tạo danh sách kết quả
		sigmoid_list = [sigmoid(i) for i in random_list]

		# In danh sách kết quả sau khi áp dụng Sigmoid
		print(sigmoid_list)

	def test_cal_factorial(self):
		# Test with known values
		self.assertEqual(cal_factorial(0), 1)
		self.assertEqual(cal_factorial(1), 1)
		self.assertEqual(cal_factorial(5), 120)
		self.assertEqual(cal_factorial(10), 3628800)

		# Test with negative value
		with self.assertRaises(ValueError):
			cal_factorial(-1)

	def test_approximate_sin(self):
		# Test with known values and comparison to math.sin
		self.assertAlmostEqual(approximate_sin(0, 5), math.sin(0), places = 5)
		self.assertAlmostEqual(approximate_sin(math.pi / 2, 5), math.sin(math.pi / 2), places = 5)
		self.assertAlmostEqual(approximate_sin(math.pi / 4, 5), math.sin(math.pi / 4), places = 5)

	def test_approximate_cos(self):
		# Test with known values and comparison to math.cos
		self.assertAlmostEqual(approximate_cos(0, 5), math.cos(0), places = 5)
		self.assertAlmostEqual(approximate_cos(math.pi / 2, 5), math.cos(math.pi / 2), places = 5)
		# self.assertAlmostEqual(approximate_cos(math.pi, 5), math.cos(math.pi), places = 5)
		self.assertAlmostEqual(approximate_cos(math.pi / 4, 5), math.cos(math.pi / 4), places = 5)

	def test_approximate_sinh(self):
		# Test with known values and comparison to math.sinh
		self.assertAlmostEqual(approximate_sinh(0, 5), math.sinh(0), places = 5)
		self.assertAlmostEqual(approximate_sinh(1, 5), math.sinh(1), places = 5)
		self.assertAlmostEqual(approximate_sinh(-1, 5), math.sinh(-1), places = 5)
		self.assertAlmostEqual(approximate_sinh(0.5, 5), math.sinh(0.5), places = 5)

	def test_approximate_cosh(self):
		# Test with known values and comparison to math.cosh
		self.assertAlmostEqual(approximate_cosh(0, 5), math.cosh(0), places = 5)
		self.assertAlmostEqual(approximate_cosh(1, 5), math.cosh(1), places = 5)
		self.assertAlmostEqual(approximate_cosh(-1, 5), math.cosh(-1), places = 5)
		self.assertAlmostEqual(approximate_cosh(0.5, 5), math.cosh(0.5), places = 5)

	def test_equal_arrays(self):
		y_true = [1, 2, 3]
		y_pred = [1, 2, 3]
		n = 2
		self.assertEqual(calculate_mdnre(y_true, y_pred, n), 0.0)

	def test_single_element(self):
		y_true = [1]
		y_pred = [4]
		n = 2
		self.assertEqual(calculate_mdnre(y_true, y_pred, n), 1.7320508075688772)

	def test_multiple_elements(self):
		y_true = [1, 2, 3]
		y_pred = [2, 3, 4]
		n = 2
		expected_result = (1 ** (1 / 2) + 1 ** (1 / 2) + 1 ** (1 / 2)) / 3
		self.assertAlmostEqual(calculate_mdnre(y_true, y_pred, n), expected_result)

	def test_different_n(self):
		y_true = [1, 8, 27]
		y_pred = [1, 27, 8]
		n = 3
		expected_result = (0 ** (1 / 3) + 19 ** (1 / 3) + 19 ** (1 / 3)) / 3
		self.assertAlmostEqual(calculate_mdnre(y_true, y_pred, n), expected_result)

	def test_value_error(self):
		y_true = [1, 2, 3]
		y_pred = [1, 2]
		n = 2
		with self.assertRaises(ValueError):
			calculate_mdnre(y_true, y_pred, n)

	def test_zero_difference(self):
		y_true = [0, 0, 0]
		y_pred = [0, 0, 0]
		n = 2
		self.assertEqual(calculate_mdnre(y_true, y_pred, n), 0.0)


if __name__ == '__main__':
	unittest.main()
