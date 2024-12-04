import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('output.csv')

df = df[[
    'Bạn quan tâm đến loại sản phẩm nào?',
    'Bạn thường quan tâm đến sản phẩm nào của Việt Tiến?',
    'Bạn thường mua hàng quan tâm đến điều gì?',
    'Giá sản phẩm đã tương xứng với chất lượng sản phẩm chưa?',
    'Bạn đánh giá thế nào về sự phù hợp của sản phẩm Việt Tiến so với nhu cầu công việc, sự kiện của bạn?',
    'Bạn thấy chất lượng sản phẩm Việt Tiến như thế nào?'
]]

df_selected = df[['Bạn quan tâm đến loại sản phẩm nào?', 'Bạn thường quan tâm đến sản phẩm nào của Việt Tiến?']]
df_melted = df_selected.melt(var_name='Câu hỏi', value_name='Trả lời')

plt.figure(figsize=(10, 8))
ax = sns.countplot(data=df_melted, y='Trả lời', hue='Câu hỏi', palette="Set2")

plt.title('Trực quan hóa dữ liệu cho hai câu hỏi', fontsize=16)
plt.xlabel('Số lượng', fontsize=14)
plt.ylabel('Câu hỏi', fontsize=14)

ax.invert_yaxis()

for p in ax.patches:
    width = p.get_width()
    y = p.get_y() + p.get_height() / 2.

    ax.annotate(f'{width}',
                (width, y),
                ha='left', va='center',
                fontsize=12, color='black', fontweight='bold',
                xytext=(10, 0), textcoords='offset points')

plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 8))

sns.countplot(data=df, x="Bạn thường mua hàng quan tâm đến điều gì?", hue="Bạn thường mua hàng quan tâm đến điều gì?", palette="Set2", legend=False)

plt.title(f'Điều quan tâm đến là gì', fontsize=16)
plt.xlabel("Bạn thường mua hàng quan tâm đến điều gì?", fontsize=14)
plt.ylabel('Số lượng', fontsize=14)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 6))
df['Giá sản phẩm đã tương xứng với chất lượng sản phẩm chưa?'].value_counts().plot.pie(
    autopct='%1.1f%%',
    startangle=90,
    colors=['#ff9999', '#66b3ff', '#99ff99']
)
plt.title('Giá sản phẩm đã tương xứng với chất lượng sản phẩm chưa?', fontsize=16)
plt.ylabel('')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 6))
df['Bạn đánh giá thế nào về sự phù hợp của sản phẩm Việt Tiến so với nhu cầu công việc, sự kiện của bạn?'].value_counts().plot.pie(
    autopct='%1.1f%%',
    startangle=90,
    colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
)
plt.title('Bạn đánh giá thế nào về sự phù hợp\ncủa sản phẩm Việt Tiến so với\nnhu cầu công việc của bạn?', fontsize=16)
plt.ylabel('')
plt.tight_layout()
plt.show()


df_selected = df[['Bạn thường mua hàng quan tâm đến điều gì?', 'Giá sản phẩm đã tương xứng với chất lượng sản phẩm chưa?']]

plt.figure(figsize=(10, 6))
ax = sns.countplot(data=df_selected,
                   x='Bạn thường mua hàng quan tâm đến điều gì?',
                   hue='Giá sản phẩm đã tương xứng với chất lượng sản phẩm chưa?',
                   palette='Set2')

plt.title('Sự quan tâm đến các yếu tố khi mua hàng và sự tương xứng giữa giá và chất lượng sản phẩm', fontsize=16)
plt.xlabel('Điều quan tâm khi mua hàng', fontsize=14)
plt.ylabel('Số lượng', fontsize=14)

plt.xticks(rotation=45, ha='right', fontsize=12)

for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x = p.get_x() + width / 2
    y = p.get_y() + height / 2
    ax.annotate(f'{height}',
                (x, y),
                ha='center', va='center',
                fontsize=12, color='black', fontweight='bold')

plt.tight_layout()
plt.show()
