# Viết chương trình tính khoảng cách chỉnh sửa tối thiểu Levenshtein. Khoảng cách Levenshtein thể
# hiện khoảng cách khác biệt giữa 2 chuỗi ký tự. Khoảng cách Levenshtein giữa chuỗi S và chuỗi T
# là số bước ít nhất biến chuỗi S thành chuỗi T thông qua 3 phép biến đổi là:
# • Xoá một ký tự
# • Thêm một ký tự
# • Thay thế ký tự này bằng ký tự khác


def levenshtein_distance( s: str, t: str ) -> int:
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


def main():
	# Ví dụ sử dụng
	s = "kitten"
	t = "sitting"
	print(f"Khoảng cách Levenshtein giữa '{s}' và '{t}' là: {levenshtein_distance(s, t)}")


if __name__ == '__main__':
	main()
