# Câu hỏi trắc nghiệm

# Câu hỏi 1:(Code) Hoàn thành chương trình sau với mô tả bài toán từ câu I.1. Đầu ra của chương trình
# dưới đây là gì?


def max_kernel(num_list, k):
	# Lấy độ dài của danh sách
	length_list = len(num_list)
	# Nếu danh sách rỗng, trả về danh sách rỗng
	if length_list <= 0:
		return num_list
	# Nếu k bằng 0, đưa ra thông báo lỗi
	if k == 0:
		print("K phải lớn hơn hoặc bằng 1")
		return list()
	# Khởi tạo giá trị lớn nhất là phần tử đầu tiên của danh sách
	max_numb = num_list[0]
	# Tạo danh sách rỗng để lưu trữ các giá trị lớn nhất
	max_numb_list = list()
	# Duyệt qua danh sách từ 0 đến độ dài của danh sách trừ đi k cộng 1
	for i in range(0, length_list - k + 1):
		# Duyệt qua k phần tử tiếp theo từ vị trí hiện tại
		for j in range(i, i + k):
			# Nếu tìm thấy phần tử lớn hơn, cập nhật giá trị lớn nhất
			if num_list[j] > max_numb:
				max_numb = num_list[j]
		# Thêm giá trị lớn nhất vào danh sách kết quả
		max_numb_list.append(max_numb)
	return max_numb_list


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))
assert max_kernel([], 3) == []
assert max_kernel([3, 4, 5, 1, -44], 0) == []


# Câu hỏi 2:(Code) Hoàn thành chương trình sau với mô tả bài toán từ câu I.2. Đầu ra của chương trình
# dưới đây là gì?

def character_count(word):
	# Khởi tạo từ điển kết quả
	result = dict()
	# Loại bỏ khoảng cách của từ đầu vào
	word = word.strip()
	# Duyệt qua từng ký tự trong từ đầu vào
	for i, letter in enumerate(word):
		# Nếu ký tự không thuộc bảng chữ cái, đưa ra thông báo lỗi
		if not letter.isalpha():
			print(f"Từ [{i}] ko thuộc bảng chữ cái")
			return dict()
		# Nếu ký tự chưa có trong từ điển kết quả, thêm vào với giá trị 1
		if letter not in result:
			result[letter] = 1
		else:
			# Nếu ký tự đã có trong từ điển kết quả, tăng giá trị lên 1
			result[letter] = result.get(letter) + 1

	# Trả về từ điển kết quả được sắp xếp theo số lần xuất hiện của các ký tự
	return dict(sorted(result.items(), key = lambda item: item[1]))


assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))
assert character_count('smiles1') == dict()

# Câu hỏi 3:(Code) Hoàn thành chương trình sau với mô tả bài toán từ câu I.3. Đầu ra của chương trình
# dưới đây là gì?

def count_word(path: str) -> dict:
	"""
	Hàm này đếm số lần xuất hiện của mỗi từ trong tệp văn bản đầu vào và trả về một từ điển
	chứa các từ và số lần xuất hiện của chúng, được sắp xếp theo thứ tự tăng dần của số lần xuất hiện.
	"""

	# Khởi tạo từ điển kết quả
	result = dict()

	# Đọc danh sách các từ từ tệp văn bản
	list_word = read(path, separator = ' ')
	if list_word is None:
		return dict()
	# Đếm số lần xuất hiện của các từ trong danh sách
	count_word_list(list_word, result)

	# Trả về từ điển kết quả được sắp xếp theo số lần xuất hiện của các từ
	return dict(sorted(result.items(), key = lambda item: item[1]))


def count_word_list(list_word: list, result: dict):
	"""
	Hàm đệ quy này đếm số lần xuất hiện của mỗi từ trong danh sách từ và cập nhật từ điển kết quả.
	"""

	# Duyệt qua từng từ trong danh sách
	for i, word in enumerate(list_word):
		# Nếu từ là một danh sách con, gọi đệ quy để xử lý danh sách con đó
		if type(word) is list:
			count_word_list(word, result)
		else:
			# Nếu từ bắt đầu bằng chữ hoa, bỏ qua
			if word.istitle():
				continue
			# Nếu từ chưa có trong từ điển kết quả, thêm vào với giá trị 1
			if word not in result:
				result[word] = 1
			else:
				# Nếu từ đã có trong từ điển kết quả, tăng giá trị lên 1
				result[word] = result.get(word) + 1


def read(path, mode = 'r', separator = ','):
	"""
	Hàm này đọc dữ liệu từ tệp văn bản đầu vào và trả về danh sách các từ được phân tách
	bởi ký tự phân tách (separator).
	"""

	try:
		# Mở tệp và đọc nội dung
		with open(path, mode) as file:
			du_lieu = [line.strip().split(separator) for line in file.readlines()]
		return du_lieu
	except Exception as e:
		# In thông báo lỗi nếu có lỗi xảy ra khi đọc tệp
		print(f"Có lỗi xảy ra khi đọc data: {e}")
		return None


file_path = 'P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])
file_path = 'P1_data_1.txt'
result = count_word(file_path)
assert result == dict()


# Câu hỏi 4:(Code) Hoàn thành chương trình sau với mô tả bài toán từ câu I.4. Đầu ra của chương trình
# dưới đây là gì?

def levenshtein_distance(s, t):
	"""
		Hàm này tính khoảng cách Levenshtein giữa hai chuỗi s và t.
		Khoảng cách Levenshtein là số phép biến đổi tối thiểu (chèn, xóa, thay thế) cần thiết
		để biến chuỗi s thành chuỗi t.
		"""

	m, n = len(s), len(t)

	# Tạo một bảng 2D để lưu trữ khoảng cách giữa các tiền tố của s và t
	dp = [[0] * (n + 1) for _ in range(m + 1)]

	# Khởi tạo bảng với các giá trị cơ sở
	# Khoảng cách từ chuỗi rỗng đến các tiền tố của s
	for i in range(m + 1):
		dp[i][0] = i
	# Khoảng cách từ chuỗi rỗng đến các tiền tố của t
	for j in range(n + 1):
		dp[0][j] = j

	# Tính toán khoảng cách Levenshtein
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			# Nếu ký tự hiện tại của s và t giống nhau, không cần phép biến đổi nào
			if s[i - 1] == t[j - 1]:
				dp[i][j] = dp[i - 1][j - 1]
			else:
				# Nếu không, chọn phép biến đổi có chi phí nhỏ nhất trong ba phép biến đổi
				dp[i][j] = min(dp[i - 1][j] + 1,  # Xóa
				               dp[i][j - 1] + 1,  # Thêm
				               dp[i - 1][j - 1] + 1)  # Thay thế

	# Khoảng cách Levenshtein là giá trị ở góc dưới cùng bên phải của bảng
	return dp[m][n]


assert levenshtein_distance("hi", "hello") == 4
print(levenshtein_distance("hola", "hello"))


# Câu hỏi 5:(Code) Hoàn thành chương trình sau. Đầu ra của chương trình dưới đây là gì?
def check_the_number(numb):
	list_of_numbers = []
	result = ""
	for i in range(1, 5):
		# Your code here
		# Su dung append them i vao trong list_of_number
		list_of_numbers.append(i)

	if numb in list_of_numbers:
		result = "True"
	if numb not in list_of_numbers:
		result = "False"
	return result


N = 7
assert check_the_number(N) == "False"
N = 2
results = check_the_number(N)
print(results)


# Câu hỏi 6:(Code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?
def my_function(data, max, min):
	result = []
	for i in data:
		# Your code here
		# Neu i < min thi them min vao result
		if i < min:
			result.append(min)
		elif i > max:
			result.append(max)
		else:
			result.append(i)
	return result


my_list = [5, 2, 5, 0, 1]
max = 1
min = 0
assert my_function(max = max, min = min, data = my_list) == [1, 1, 1, 0, 1]
my_list = [10, 2, 5, 0, 1]
max = 2
min = 1
print(my_function(max = max, min = min, data = my_list))


# Câu hỏi 7:(code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?


def my_function(x, y):
	# Your code here
	# Su dung extend de noi y vao x
	# return x
	x.extend(y)

	return x


list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]

assert my_function(list_num1, my_function(list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]

print(my_function(list_num1, my_function(list_num2, list_num3)))


# Câu hỏi 8:(code) Hãy hoàn thành chương trình tìm phần tử có giá trị nhỏ nhất trong một list dưới
# đây. Đầu ra của chương trình là gì?


def find_min(n: list[int]) -> int:
	# Your code here
	min_num = n[0]
	for element in n:
		if min_num > element:
			min_num = element
	return min_num


my_list = [1, 22, 93, -100]
assert find_min(my_list) == -100

my_list = [1, 2, 3, -1]
print(find_min(my_list))


# Câu hỏi 9:(code) Hãy hoàn thành chương trình tìm phần tử có giá trị lớn nhất trong một list dưới
# đây. Đầu ra của chương trình là gì?

def find_max(n: list[int]) -> int:
	# Your code here
	max_numb = n[0]
	for element in n:
		if max_numb < element:
			max_numb = element
	return max_numb


my_list = [1001, 9, 100, 0]
assert find_max(my_list) == 1001

my_list = [1, 9, 9, 0]
print(find_max(my_list))


# Câu hỏi 10:(code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?
def valdate_numb(integers, number = 1):
	return any(  # Your code here : Thuc hien duyet tung phan tu trong integers , so sanh
		# tung phan tu voi number , neu bang nhau tra ve True , khac nhau tra ve false
		# vi du: integers = [1 , 2 , 3] , number = 2 , ban se tao ra list [False ,True , False ]

		[True if element == number else False for element in integers]
	)


my_list = [1, 3, 9, 4]
assert valdate_numb(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(valdate_numb(my_list, 2))


# Câu hỏi 11:(code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?

def my_function(list_nums = None):
	if list_nums is None:
		list_nums = [0, 1, 2]
	var = 0
	for i in list_nums:
		var += i
	# Your code here : Tra ve gia tri trung binh cua list bang cach chia var cho
	# so luong phan tu trong list_mums
	return var / len(list_nums)


assert my_function([4, 6, 8]) == 6
print(my_function())


# Câu hỏi 12:(code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình dưới đây là gì?

def my_function(data):
	var = []
	for i in data:
		# Your code here
		# Neu i chia het cho 3 thi them i vao list var
		if i % 3 == 0:
			var.append(i)

	return var


assert my_function([3, 9, 4, 5]) == [3, 9]
print(my_function([1, 2, 3, 5, 6]))


# Câu hỏi 13:(code) Hãy hoàn thành chương trình sau đây thực hiện tính giai thừa của 1 số. Đầu ra
# của chương trình dưới đây là gì?


def tinh_giai_thua(y):
	var = 1
	while (y > 1):
		# Your code here
		var *= y
		y -= 1
	return var


assert tinh_giai_thua(8) == 40320
print(tinh_giai_thua(4))


# Câu hỏi 14:(code) Hãy hoàn thành chương trình đảo ngược chuỗi dưới đây. Đầu ra của chương trình
# là gì?

def reverse_word(x):
	# your code here
	return x[::-1]


x = 'I can do it'
assert reverse_word(x) == "ti od nac I"

x = 'apricot'
print(reverse_word(x))


# Câu hỏi 15:(code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?
def is_greater(x):
	# Your code here
	# Neu x >0 tra ve 'T ', nguoc lai tra ve 'N'
	return 'T' if x > 0 else 'N'


def validate_numb(data):
	res = [is_greater(x) for x in data]
	return res


data = [10, 0, -10, -1]
assert validate_numb(data) == ['T', 'N', 'N', 'N']

data = [2, 3, 5, -1]
print(validate_numb(data))


# Câu hỏi 16:(code) Hãy hoàn thành chương trình dưới đây để loại bỏ những phần tử trùng nhau. Đầu
# ra của chương trình là gì?


def is_duplicate(x, data):
	for i in data:
		if x == i:
			return 0
	return 1


def my_function(data):
	res = []
	for i in data:
		if is_duplicate(i, res):
			res.append(i)
	return res


lst = [10, 10, 9, 7, 7]
assert my_function(lst) == [10, 9, 7]

lst = [9, 9, 8, 1, 1]
print(my_function(lst))
