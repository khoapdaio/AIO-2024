import cv2
import numpy as np

size = (678, 381)

bg1_image = cv2.imread('../../../data/module2/week2/GreenBackground.png', 1)
bg1_image = cv2.resize(bg1_image, size)

ob_image = cv2.imread('../../../data/module2/week2/Object.png', 1)
ob_image = cv2.resize(ob_image, size)

bg2_image = cv2.imread('../../../data/module2/week2/NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image, size)


# Cách 1:
def compute_binary_mask_custom(bg_img, input_img):
	# Chuyển đổi các ảnh sang không gian màu HSV để dễ dàng xử lý
	hsv_object = cv2.cvtColor(input_img, cv2.COLOR_BGR2HSV)
	hsv_bg1 = cv2.cvtColor(bg_img, cv2.COLOR_BGR2HSV)

	# Định nghĩa dải màu xanh lá cây để tạo mask
	lower_green = np.array([35, 100, 100])
	upper_green = np.array([85, 255, 255])

	# unique_colors = np.unique(hsv_bg1.reshape(-1, hsv_bg1.shape[2]), axis=0)[0]

	# Tạo mask cho vùng màu xanh lá cây
	mask = cv2.inRange(hsv_object, lower_green, upper_green)

	# Invert mask để lấy vùng của đối tượng
	mask_inv = cv2.bitwise_not(mask)

	# Tạo mask binary với các giá trị 0 là background và 1 là object
	binary_mask = mask_inv // 255
	return binary_mask

def replace_background_custom(bg1_image, bg2_image, ob_image):
	binary_mask = compute_binary_mask_custom(bg1_image, ob_image)
	# Tạo ảnh output
	output = np.where(binary_mask[..., None] == 1, ob_image, bg2_image)

	return output


cv2.imshow('Result custom 1', replace_background_custom(bg1_image, bg2_image, ob_image))
cv2.waitKey(0)
cv2.destroyAllWindows()


# Cách 2

def compute_difference(bg_img, input_img):
	# Chuyển đổi các ảnh sang grayscale
	gray_object = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
	gray_bg = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)

	# Sử dụng background subtraction để lấy mask của object
	foreground_mask = cv2.absdiff(gray_object, gray_bg)
	return foreground_mask

def compute_binary_mask(difference_single_channel):
	# Ngưỡng hóa mask để tạo ảnh binary
	_, binary_mask = cv2.threshold(difference_single_channel, 0, 255, cv2.THRESH_BINARY)

	# Tạo mask binary với các giá trị 0 là background và 1 là object
	binary_mask = binary_mask // 255
	return binary_mask


def replace_background(bg1_image, bg2_image, ob_image):
	difference_single_channel = compute_difference(
		bg1_image,
		ob_image
	)

	binary_mask = compute_binary_mask(difference_single_channel)
	# Tạo ảnh output
	output = np.where(binary_mask[..., None] == 1, ob_image, bg2_image)

	return output


# Hiển thị ảnh kết quả
cv2.imshow('Result', replace_background(bg1_image, bg2_image, ob_image))
cv2.waitKey(0)
cv2.destroyAllWindows()
