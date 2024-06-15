# Câu hỏi trắc nghiệm
from src.module1.week2 import character_count, max_kernel, count_word, levenshtein_distance

# Câu hỏi 1:(Code) Hoàn thành chương trình sau với mô tả bài toán từ câu I.1. Đầu ra của chương trình
# dưới đây là gì?

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))


# Câu hỏi 2:(Code) Hoàn thành chương trình sau với mô tả bài toán từ câu I.2. Đầu ra của chương trình
# dưới đây là gì?

print(character_count('smiles'))

# Câu hỏi 3:(Code) Hoàn thành chương trình sau với mô tả bài toán từ câu I.3. Đầu ra của chương trình
# dưới đây là gì?

file_path = 'data/module1/week2/P1_data.txt'
result = count_word(file_path)
print(result['man'])


# Câu hỏi 4:(Code) Hoàn thành chương trình sau với mô tả bài toán từ câu I.4. Đầu ra của chương trình
# dưới đây là gì?


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


N = 2
results = check_the_number(N)
print(results)


# Câu hỏi 6:(Code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?
def validate_data(data, max, min):
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



my_list = [10, 2, 5, 0, 1]
max = 2
min = 1
print(validate_data(max = max, min = min, data = my_list))


# Câu hỏi 7:(code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?


def add_list(x, y):
	# Your code here
	# Su dung extend de noi y vao x
	# return x
	x.extend(y)

	return x


list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]

print(add_list(list_num1, add_list(list_num2, list_num3)))


# Câu hỏi 8:(code) Hãy hoàn thành chương trình tìm phần tử có giá trị nhỏ nhất trong một list dưới
# đây. Đầu ra của chương trình là gì?


def find_min(n: list[int]) -> int:
	# Your code here
	min_num = n[0]
	for element in n:
		if min_num > element:
			min_num = element
	return min_num


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



my_list = [1, 9, 9, 0]
print(find_max(my_list))


# Câu hỏi 10:(code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?
def validate_numb(integers, number = 1):
	return any(  # Your code here : Thuc hien duyet tung phan tu trong integers , so sanh
		# tung phan tu voi number , neu bang nhau tra ve True , khac nhau tra ve false
		# vi du: integers = [1 , 2 , 3] , number = 2 , ban se tao ra list [False ,True , False ]

		[True if element == number else False for element in integers]
	)


my_list = [1, 2, 3, 4]
print(validate_numb(my_list, 2))


# Câu hỏi 11:(code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình là gì?

def tinh_gia_tri_tb(list_nums = None):
	if list_nums is None:
		list_nums = [0, 1, 2]
	var = 0
	for i in list_nums:
		var += i
	# Your code here : Tra ve gia tri trung binh cua list bang cach chia var cho
	# so luong phan tu trong list_mums
	return var / len(list_nums)


assert tinh_gia_tri_tb([4, 6, 8]) == 6
print(tinh_gia_tri_tb())


# Câu hỏi 12:(code) Hãy hoàn thành chương trình dưới đây. Đầu ra của chương trình dưới đây là gì?

def tim_so_chia_het_3(data):
	var = []
	for i in data:
		# Your code here
		# Neu i chia het cho 3 thi them i vao list var
		if i % 3 == 0:
			var.append(i)

	return var

print(tim_so_chia_het_3([1, 2, 3, 5, 6]))


# Câu hỏi 13:(code) Hãy hoàn thành chương trình sau đây thực hiện tính giai thừa của 1 số. Đầu ra
# của chương trình dưới đây là gì?


def tinh_giai_thua(y):
	var = 1
	while (y > 1):
		# Your code here
		var *= y
		y -= 1
	return var


print(tinh_giai_thua(4))


# Câu hỏi 14:(code) Hãy hoàn thành chương trình đảo ngược chuỗi dưới đây. Đầu ra của chương trình
# là gì?

def reverse_word(x):
	# your code here
	return x[::-1]


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



data = [2, 3, 5, -1]
print(validate_numb(data))


# Câu hỏi 16:(code) Hãy hoàn thành chương trình dưới đây để loại bỏ những phần tử trùng nhau. Đầu
# ra của chương trình là gì?


def is_duplicate(x, data):
	for i in data:
		if x == i:
			return 0
	return 1


def check_dup_value(data):
	res = []
	for i in data:
		if is_duplicate(i, res):
			res.append(i)
	return res



lst = [9, 9, 8, 1, 1]
print(check_dup_value(lst))
