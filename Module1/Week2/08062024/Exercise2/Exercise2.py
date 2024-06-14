# Viết function trả về một dictionary đếm số lượng chữ xuất hiện trong một từ, với key là chữ cái
# và value là số lần xuất hiện
# • Input: một từ
# • Output: dictionary đếm số lần các chữ xuất hiện
# • Note: Giả sử các từ nhập vào đều có các chữ cái thuộc [a-z] hoặc [A-Z]


def count_char(word: str) -> dict:
	"""
	Hàm này đếm số lần xuất hiện của mỗi ký tự trong từ đầu vào và trả về một từ điển
	chứa các ký tự và số lần xuất hiện của chúng, được sắp xếp theo thứ tự tăng dần
	của số lần xuất hiện.
	"""
	# Loại bỏ khoảng cách của từ đầu vào
	word = word.strip()
	# Khởi tạo từ điển kết quả
	result = dict()

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


def main():
	string = 'Happiness'
	result = {'H': 1, 'a': 1, 'i': 1, 'n': 1, 'e': 1, 'p': 2, 's': 2}
	assert count_char(string) == result
	string= 'Happines0'
	assert count_char(string) == dict()


if __name__ == '__main__':
	main()
