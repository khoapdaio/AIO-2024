import math


def elu(x, alpha = 1.0):
	"""
    Hàm mô phỏng ELU (Exponential Linear Unit) Function.

    Args:
      x: Giá trị đầu vào.
      alpha: Tham số điều chỉnh độ dốc của phần âm. Giá trị mặc định là 1.0.

    Returns:
      Giá trị đầu ra sau khi áp dụng hàm ELU.
    """
	if x >= 0:
		return x
	else:
		return alpha * (math.exp(x) - 1)
