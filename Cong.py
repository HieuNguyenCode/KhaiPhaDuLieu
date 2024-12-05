import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc file CSV
file_path = "output.csv"  # Thay đổi theo đường dẫn file của bạn
data = pd.read_csv(file_path)
data.info()

# Tạo figure và subplots
fig, axes = plt.subplots(3, 2, figsize=(18, 18))  # Tạo lưới 3 hàng x 2 cột

# 1. Kênh mạng xã hội phổ biến
sns.countplot(
    y='Thời gian rảnh bạn thường sử dụng mạng xã hội nào?',
    data=data,
    order=data['Thời gian rảnh bạn thường sử dụng mạng xã hội nào?'].value_counts().index,
    ax=axes[0, 0]
)
axes[0, 0].set_title("Kênh mạng xã hội phổ biến")
axes[0, 0].set_xlabel("Số lượng")
axes[0, 0].set_ylabel("Kênh mạng xã hội")

# 2. Loại nội dung quảng cáo thu hút
sns.countplot(
    y='Những loại nội dung quảng cáo dưới dạng nào thu hút bạn nhất?',
    data=data,
    order=data['Những loại nội dung quảng cáo dưới dạng nào thu hút bạn nhất?'].value_counts().index,
    ax=axes[0, 1]
)
axes[0, 1].set_title("Loại nội dung quảng cáo thu hút nhất")
axes[0, 1].set_xlabel("Số lượng")
axes[0, 1].set_ylabel("Loại nội dung")

# 3. Mức độ hấp dẫn của chương trình khuyến mãi
sns.countplot(
    y='Bạn có thấy các chương trình khuyến mãi của chúng tôi hấp dẫn không?',
    data=data,
    order=data['Bạn có thấy các chương trình khuyến mãi của chúng tôi hấp dẫn không?'].value_counts().index,
    ax=axes[1, 0]
)
axes[1, 0].set_title("Mức độ hấp dẫn của chương trình khuyến mãi")
axes[1, 0].set_xlabel("Số lượng")
axes[1, 0].set_ylabel("Đánh giá")

# 4. Yếu tố khiến khách hàng mua sản phẩm
sns.countplot(
    y='Điều gì khiến bạn chọn mua sản phẩm của Việt Tiến vì nhãn hàng khác?',
    data=data,
    order=data['Điều gì khiến bạn chọn mua sản phẩm của Việt Tiến vì nhãn hàng khác?'].value_counts().index,
    ax=axes[1, 1]
)
axes[1, 1].set_title("Yếu tố thu hút khách hàng mua sản phẩm")
axes[1, 1].set_xlabel("Số lượng")
axes[1, 1].set_ylabel("Yếu tố")

# 5. Nơi khách hàng thường thấy quảng cáo
sns.countplot(
    y='Bạn thường thấy các quảng cáo của chúng tôi ở đâu nhiều nhất?',
    data=data,
    order=data['Bạn thường thấy các quảng cáo của chúng tôi ở đâu nhiều nhất?'].value_counts().index,
    ax=axes[2, 0]
)
axes[2, 0].set_title("Nơi khách hàng thường thấy quảng cáo của Việt Tiến")
axes[2, 0].set_xlabel("Số lượng")
axes[2, 0].set_ylabel("Kênh quảng cáo")

# Loại bỏ subplot thừa
fig.delaxes(axes[2, 1])

# Tăng khoảng cách giữa các subplots
plt.tight_layout()
plt.show()



# Đọc file CSV


# Lọc các câu hỏi liên quan đến marketing
marketing_columns = [
    'Thời gian rảnh bạn thường sử dụng mạng xã hội nào?',
    'Những loại nội dung quảng cáo dưới dạng nào thu hút bạn nhất?',
    'Bạn có thấy các chương trình khuyến mãi của chúng tôi hấp dẫn không?',
    'Điều gì khiến bạn chọn mua sản phẩm của Việt Tiến vì nhãn hàng khác?',
    'Bạn thường thấy các quảng cáo của chúng tôi ở đâu nhiều nhất?'
]

# Thiết lập kích thước tổng thể của figure
fig, axes = plt.subplots(3, 2, figsize=(15, 15))
axes = axes.flatten()  # Chuyển mảng axes thành 1D để dễ truy cập

# Vẽ từng biểu đồ tròn
for i, column in enumerate(marketing_columns):
    # Lấy dữ liệu giá trị và tần suất
    value_counts = data[column].value_counts()
    labels = value_counts.index
    sizes = value_counts.values

    # Vẽ biểu đồ tròn
    axes[i].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 10})
    axes[i].set_title(column, fontsize=12)

# Xóa ô thừa nếu không đủ câu hỏi
for j in range(len(marketing_columns), len(axes)):
    fig.delaxes(axes[j])

# Tăng khoảng cách giữa các biểu đồ
plt.tight_layout()
plt.show()
