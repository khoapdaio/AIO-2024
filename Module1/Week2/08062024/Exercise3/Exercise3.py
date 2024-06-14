# Viết function đọc các câu trong một file txt, đếm số lượng các từ xuất hiện và trả về một dictionary
# với key là từ và value là số lần từ đó xuất hiện.
# • Input: Đường dẫn đến file txt
# • Output: dictionary đếm số lần các từ xuất hiện
# • Note:
# – Giả sử các từ trong file txt đều có các chữ cái thuộc [a-z] hoặc [A-Z]
# – Không cần các thao tác xử lý string phức tạp nhưng cần xử lý các từ đều là viết
# thường
# – Các bạn dùng lệnh này để download
# !gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko

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


def main():
	file_path = 'P1_data.txt'

	result = {'conquers': 1, 'himself': 1, 'mightiest': 1, 'warrior': 1, 'not': 1, 'but': 1, 'rather': 1, 'value': 1,
	          'courage': 1, 'makes': 1, 'majority': 1, 'secret': 1, 'be': 1, 'ready': 1, 'opportunity': 1, 'profit': 1,
	          'from': 1, 'mistakes': 1, 'and': 1, 'try': 1, 'again': 1, 'different': 1, 'way': 1, 'lay': 1, 'firm': 1,
	          'foundation': 1, 'bricks': 1, 'others': 1, 'have': 1, 'thrown': 1, 'at': 1, 'him': 1, 'usually': 1,
	          'those': 1, 'are': 1, 'too': 1, 'busy': 1, 'looking': 1, 'cannot': 1, 'solve': 1, 'problems': 1,
	          'kind': 1, 'thinking': 1, 'employed': 1, 'came': 1, 'up': 1, 'them': 1, 'small': 1, 'positive': 1,
	          'thought': 1, 'morning': 1, 'change': 1, 'your': 1, 'whole': 1, 'day': 1, 'everything': 1, 'if': 1,
	          'just': 1, 'help': 1, 'enough': 1, 'other': 1, 'people': 1, 'what': 1, 'they': 1, 'become': 2,
	          'success': 2, 'life': 2, 'his': 2, 'when': 2, 'it': 2, 'comes': 2, 'successful': 2, 'will': 2, 'one': 2,
	          'we': 2, 'get': 2, 'you': 2, 'want': 2, 'who': 3, 'is': 3, 'to': 3, 'for': 3, 'can': 3, 'the': 4, 'of': 4,
	          'with': 4, 'in': 4, 'a': 6, 'man': 6}
	assert count_word(file_path) == result
	file_path = 'P2_data_1.txt'
	assert count_word(file_path) == dict()


if __name__ == '__main__':
	main()
