import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file output.csv
df = pd.read_csv("output.csv")

# Các câu hỏi cần vẽ biểu đồ
questions = [
    'Thời điểm nào trong ngày bạn mua hàng nhiều nhất?',
    'Bạn quan tâm đến loại sản phẩm nào?',
    'Bạn thường mua sản phẩm ở đâu?',
    'Bạn thường quan tâm đến sản phẩm nào của Việt Tiến?'

]

# Lặp qua từng câu hỏi để vẽ biểu đồ
for question in questions:
    # Lấy dữ liệu câu trả lời và tần suất xuất hiện
    data = df[question].value_counts()

    # Vẽ biểu đồ tròn
    plt.figure(figsize=(8, 8))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 12})
    plt.title(f'Biểu đồ tròn: {question}', fontsize=14)
    plt.axis('equal')  # Đảm bảo hình tròn
    plt.show()
