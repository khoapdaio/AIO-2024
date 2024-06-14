# Cho một list các số nguyên num_list và một sliding window có kích thước size k di
# chuyển từ trái sang phải. Mỗi lần dịch chuyển 1 vị trí sang phải có thể nhìn thấy
# đươc k số trong num_list và tìm số lớn nhất trong k số này sau mỗi lần trượt k phải
# lớn hơn hoặc bằng 1


def get_max_numb_list( num_list: list, k: int = 1 ) -> list:
	"""
	Hàm này tìm giá trị lớn nhất trong mỗi đoạn con có độ dài k của danh sách đầu vào
    và trả về danh sách các giá trị lớn nhất đó.
    Nếu k bằng 1, hàm sẽ trả về chính danh sách đầu vào.
    """
	# Lấy độ dài của danh sách
	length_list = len(num_list)
	# Nếu danh sách rỗng, trả về danh sách rỗng
	if length_list <= 0:
		return num_list
	# Nếu k bằng 0, đưa ra thông báo lỗi
	if k == 0:
		raise Exception("K phải lớn hơn hoặc bằng 1")
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


def main():
	num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
	print(get_max_numb_list(num_list, 1))


if __name__ == '__main__':
	main()
