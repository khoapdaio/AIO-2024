# Bài tập 3: Phân tích dữ liệu dạng bảng
import pandas as pd

df = pd.read_csv('../../../data/module2/week1/advertising.csv')

data = df.to_numpy()
print(data)

# Câu hỏi 15: Lấy giá trị lớn nhất và chỉ mục tương ứng của nó trên cột Sales:


print(f"max => {df['Sales'].max()}")
print(f"index => {df['Sales'].idxmax()}")

# Câu hỏi 16: Giá trị trung bình của cột TV là:
print(f"mean => {df['TV'].mean()}")

# Câu hỏi 17: Số lượng bản ghi có giá trị tại cột Sales lớn hơn hoặc bằng 20 là:

print(df[df['Sales'] >= 20]['Sales'].count())

# Câu hỏi 18: Tính giá trị trung bình của cột Radio thoả mãn điều kiện giá trị tương ứng
# trên cột Sales lớn hơn hoặc bằng 15:

print(df[df['Sales'] >= 15]['Radio'].mean())

# Câu hỏi 19: Tính tổng các hàng của cột Sales với điều kiện giá trị Newspaper lớn hơn
# giá trị trung bình của cột Newspaper:

mean_newspaper = df['Newspaper'].mean()

print(f"sum_sales => {df[df['Newspaper'] > mean_newspaper]['Sales'].sum()}")


# Câu hỏi 20: Gọi giá trị trung bình của cột Sales là A. Tạo ra mảng mới scores chứa các
# giá trị Good, Average và Bad sao cho: nếu giá trị hiện tại > A => giá trị trong mảng mới
# là Good, < A thì sẽ là Bad và = A sẽ là Average. Sau đó in ra kết quả scores[7:10]


def evaluate_sales(value, mean):
	if value < mean:
		return 'Bad'
	elif value > mean:
		return 'Good'
	else:
		return 'Average'


mean_sales = df['Sales'].mean()

df['Scores'] = df['Sales'].apply(lambda e: evaluate_sales(e, mean_sales))

print(df['Scores'][7:10])


# Câu hỏi 21: Gọi giá trị trên cột Sales gần nhất với giá trị trung bình cũng chính cột
# Sales là A. Tạo ra mảng mới scores chứa các giá trị Good, Average và Bad sao cho: nếu
# giá trị hiện tại > A => giá trị trong mảng mới là Good, < A thì sẽ là Bad và = A sẽ là
# Average. Sau đó in ra kết quả scores[7:10]

# - df['Sales'] - mean_sales: Tính độ chênh lệch giữa từng giá trị trong cột Sales với giá trị trung bình.
# - abs(): Lấy giá trị tuyệt đối của độ chênh lệch.
# - argsort()[:1]: Lấy chỉ số của giá trị nhỏ nhất (gần nhất với giá trị trung bình).
# - iloc[]: Lấy giá trị tại chỉ số đó.

A = df.iloc[(df['Sales'] - mean_sales).abs().argsort()[:1]]['Sales'].values[0]
print(A)
df['Scores'] = df['Sales'].apply(lambda e: evaluate_sales(e, A))

print(df['Scores'][7:10])
