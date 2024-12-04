import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv("output.csv")

# Kiểm tra cấu trúc dữ liệu
print(df.head())

# Hàm vẽ biểu đồ tỷ lệ phần trăm cho mỗi mức trả lời
def plot_percentage(df, column_name, title):
    # Đếm tần suất của từng giá trị trong cột và tính tỷ lệ phần trăm
    value_counts = df[column_name].value_counts(normalize=True) * 100

    # Tạo danh sách màu sắc, một màu cho mỗi cột
    colors = plt.cm.get_cmap('tab10', len(value_counts))  # 'tab10' là bảng màu có nhiều màu sắc khác nhau

    # Vẽ biểu đồ cột
    plt.figure(figsize=(8, 6))
    value_counts.plot(kind='bar', color=[colors(i) for i in range(len(value_counts))])
    plt.title(title)
    plt.xlabel(column_name)
    plt.ylabel('Tỷ lệ (%)')
    plt.xticks(rotation=45, ha='right')

    # Đặt giới hạn trục y để tỷ lệ đạt 100%
    plt.ylim(0, 100)

    # Hiển thị tỷ lệ phần trăm trên mỗi cột
    for i, v in enumerate(value_counts):
        plt.text(i, v + 1, f'{v:.1f}%', ha='center', va='bottom', fontsize=10)

    plt.show()

# Vẽ biểu đồ riêng cho từng câu hỏi với tỷ lệ phần trăm
plot_percentage(df, 'Điều gì khiến bạn chọn mua sản phẩm của Việt Tiến vì nhãn hàng khác?', 'Lý do chọn mua sản phẩm Việt Tiến')
plot_percentage(df, 'Bạn thường mua sắm các sản phẩm quần áo nào ngoài Việt Tiến trong 6 tháng qua?', 'Tần suất mua sắm ngoài Việt Tiến trong 6 tháng')
plot_percentage(df, 'Bạn có thấy các chương trình khuyến mãi của các nhãn hàng khác hấp dẫn hơn so với Việt Tiến không?', 'So sánh khuyến mãi của Việt Tiến với các đối thủ cạnh tranh')
plot_percentage(df, 'Bạn cảm nhận thế nào về chất lượng dịch vụ (chăm sóc khách hàng sau và trước bán hàng) của Việt Tiến so với nhãn hàng khác?', 'So sánh chất lượng dịch vụ Việt Tiến với các đối thủ cạnh tranh')
