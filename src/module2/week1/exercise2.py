# Bài tập 2: Xử lý ảnh
import matplotlib.image as mpimg
import numpy as np

# Câu hỏi 12: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào
# phương pháp Lightness:

# Lightness: Tính giá trị trung bình của giá trị lớn nhất và nhỏ nhất cho các kênh màu: (max(R,G,B)
# + min(R,G,B))/2

img = mpimg.imread('../../../data/module2/week1/dog.jpeg')
gray_img_01 = (np.max(img[:, :3], axis = 2) + np.min(img[:, :3], axis = 2)) / 2

print(gray_img_01[0, 0])

# Câu hỏi 13: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào
# phương pháp Average:
# Average: Tính giá trị trung bình của 3 kênh màu: (R+G+B)/3

img = mpimg.imread('../../../data/module2/week1/dog.jpeg')
gray_img_02 = np.mean(img[:, :3], axis = 2)
print(gray_img_02[0, 0])

# Câu hỏi 14: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào
# phương pháp Luminosity:
# Luminosity: Nhân hệ số tương ứng của 3 kênh màu như sau: 0.21*R + 0.72*G + 0.07*B

img = mpimg.imread('../../../data/module2/week1/dog.jpeg')
gray_img_03 = 0.21 * img[..., 0] + 0.72 * img[..., 1] + 0.07 * img[..., 2]
print(gray_img_03[0, 0])
