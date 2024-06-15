def calculate_mdnre(y_true, y_pred, n):
    """
    Tính toán Sai số Trung bình Khác Biệt Gốc n (MDnRE) giữa hai mảng.

    Tham số:
        y_true (list hoặc array): Mảng giá trị thực.
        y_pred (list hoặc array): Mảng giá trị dự đoán.
        n (int): Gốc n sử dụng trong tính toán sai số (ví dụ: 2 cho căn bậc hai, 3 cho căn bậc ba).

    Trả về:
        float: Giá trị Sai số Trung bình Khác Biệt Gốc n.

    Ngoại lệ:
        ValueError: Nếu hai mảng đầu vào có độ dài khác nhau.
    """

    # Kiểm tra xem hai mảng đầu vào có cùng độ dài hay không
    if len(y_true) != len(y_pred):
        raise ValueError("Hai mảng đầu vào phải có cùng độ dài để tính MDnRE.")

    # Khởi tạo danh sách rỗng để lưu trữ sai số
    errors = []

    # Duyệt qua các phần tử tương ứng trong cả hai mảng
    for i in range(len(y_true)):
        # Tính toán sai số tuyệt đối giữa giá trị thực và giá trị dự đoán
        absolute_difference = abs(y_true[i] - y_pred[i])

        # Tính toán căn bậc n của sai số tuyệt đối
        error = absolute_difference**(1/n)

        # Thêm sai số đã tính toán vào danh sách errors
        errors.append(error)

    # Tính toán sai số trung bình bằng cách lấy trung bình các sai số
    mean_difference = sum(errors) / len(errors)

    # Trả về giá trị MDnRE đã tính toán
    return mean_difference