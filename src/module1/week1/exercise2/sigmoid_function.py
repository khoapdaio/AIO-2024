import math


def sigmoid(x):
	"""
    Hàm Sigmoid chuẩn.

    Args:
      x: Giá trị đầu vào.

    Returns:
      Giá trị đầu ra sau khi áp dụng hàm Sigmoid.
    """
	return 1 / (1 + math.exp(-x))
