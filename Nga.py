import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('output.csv')

doingutuvan = df['Đội ngũ tư vấn sản phẩm như thế nào?'].value_counts()

doinguhotro = df['Đội ngũ hỗ trợ trả hàng và hỗ trợ khách hàng như thế nào?'].value_counts()

giaohang = df['Chất lượng giao hàng thế nào?'].value_counts()

donggoi = df['Chất lượng đóng hàng thế nào?'].value_counts()

chatluongsp = df['Bạn có thấy sự thay đổi trong chất lượng sản phẩm của Việt Tiến trong thời gian gần đây?'].value_counts()

# In kết quả
print("Đội ngũ tư vấn:")
print(doingutuvan)

print("\nĐội ngũ hỗ trợ:")
print(doinguhotro)

print("\nChất lượng giao hàng:")
print(giaohang)

print("\nĐịa điểm mua hàng:")
print(donggoi)

print("\nChất lượng sản phẩm:")
print(chatluongsp)

# 1. Đội ngũ tư vấn sản phẩm
doingutuvan = df['Đội ngũ tư vấn sản phẩm như thế nào?'].value_counts(normalize=True) * 100
plt.figure(figsize=(8, 8))
doingutuvan.plot.pie(autopct='%1.1f%%', colors=sns.color_palette("Blues_d", n_colors=len(doingutuvan)), startangle=90, cmap='Blues')
plt.title("Đội ngũ tư vấn sản phẩm")
plt.ylabel('')  # Ẩn nhãn y-axis
plt.show()

# 2. Đội ngũ hỗ trợ trả hàng và hỗ trợ khách hàng
doinguhotro = df['Đội ngũ hỗ trợ trả hàng và hỗ trợ khách hàng như thế nào?'].value_counts(normalize=True) * 100
plt.figure(figsize=(8, 8))
doinguhotro.plot.pie(autopct='%1.1f%%', colors=sns.color_palette("Greens_d", n_colors=len(doinguhotro)), startangle=90, cmap='Greens')
plt.title("Đội ngũ hỗ trợ khách hàng")
plt.ylabel('')
plt.show()

# 3. Chất lượng giao hàng
giaohang = df['Chất lượng giao hàng thế nào?'].value_counts(normalize=True) * 100
plt.figure(figsize=(8, 8))
giaohang.plot.pie(autopct='%1.1f%%', colors=sns.color_palette("Oranges_d", n_colors=len(giaohang)), startangle=90, cmap='Oranges')
plt.title("Chất lượng giao hàng")
plt.ylabel('')
plt.show()

# 4. Chất lượng đóng hàng
donggoi = df['Chất lượng đóng hàng thế nào?'].value_counts(normalize=True) * 100
plt.figure(figsize=(8, 8))
donggoi.plot.pie(autopct='%1.1f%%', colors=sns.color_palette("Purples_d", n_colors=len(donggoi)), startangle=90, cmap='Purples')
plt.title("Chất lượng đóng hàng")
plt.ylabel('')
plt.show()

# 5. Chất lượng sản phẩm
chatluongsp = df['Bạn có thấy sự thay đổi trong chất lượng sản phẩm của Việt Tiến trong thời gian gần đây?'].value_counts(normalize=True) * 100
plt.figure(figsize=(8, 8))
chatluongsp.plot.pie(autopct='%1.1f%%', colors=sns.color_palette("Reds_d", n_colors=len(chatluongsp)), startangle=90, cmap='Reds')
plt.title("Chất lượng sản phẩm")
plt.ylabel('')
plt.show()
