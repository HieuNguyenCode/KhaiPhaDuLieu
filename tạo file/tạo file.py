import pandas as pd
import random

# Define possible answers for each question
questions = [
    ("Bạn có sẵn lòng trả giá cao hơn để mua sản phẩm của Việt Tiến nếu chất lượng cải thiện không?", ["Tùy thuộc vào mức tăng giá", "Có", "Không"]),
    ("Thời điểm nào trong ngày bạn mua hàng nhiều nhất?", ["0-1h", "6 – 7h", "11-12h", "17-18h", "21-23h"]),
    ("Bạn quan tâm đến loại sản phẩm nào?", ["Đồng phục", "Thời trang công sở", "Phụ kiện thời trang"]),
    ("Bạn thường mua sản phẩm ở đâu?", ["Facebook", "Tiktok", "Sàn thương mại điện tử", "Khác: ………………"]),
    ("Bạn thường dành bao nhiêu thời gian trong ngày để sử dụng mạng xã hội?", ["1 tiếng", "2 tiếng", "3 tiếng", "Khác: ………………"]),
    ("Thời gian rảnh bạn thường sử dụng mạng xã hội nào?", ["Facebook", "Tiktok", "Sàn thương mại điện tử", "Khác: ………………"]),
    ("Bạn thường quan tâm đến sản phẩm nào của Việt Tiến?", ["ves", "Thời trang công sở", "Phụ kiện (giầy da, thất lưng, ví,…)"]),
    ("Bạn thường mua hàng quan tâm đến điều gì?", ["Chất lượng sản phẩm", "Giá thành", "Thương hiệu", "Khác: ………"]),
    ("Giá sản phẩm đã tương xứng với chất lượng sản phẩm chưa?", ["Rất tương xứng", "Tương xứng", "Chưa tương xứng"]),
    ("Bạn đánh giá thế nào về sự phù hợp của sản phẩm Việt Tiến so với nhu cầu công việc, sự kiện của bạn?", ["Rất phù hợp", "Phù hợp", "Bình thường", "Không phù hợp", "Rất không phù hợp"]),
    ("Bạn thấy chất lượng sản phẩm Việt Tiến như thế nào?", ["Rất tốt", "Tốt", "ổn", "chưa tốt"]),
    ("Đội ngũ tư vấn sản phẩm như thế nào?", ["Rất nhiệt tình", "Nhiệt tình", "Thân thiện", "Chưa nhiệt tình"]),
    ("Đội ngũ hỗ trợ trả hàng và hỗ trợ khách hàng như thế nào?", ["Rất nhiệt tình", "Nhiệt tình", "Thân thiện", "Chưa nhiệt tình"]),
    ("Chất lượng giao hàng thế nào?", ["Rất nhanh chóng (từ 2 đến 3 ngày)", "Nhanh (từ 4 đến 6 ngày)", "Chưa nhanh (trên 7 ngày)"]),
    ("Chất lượng đóng hàng thế nào?", ["Rất cẩn thận", "Cẩn thận", "Chưa cẩn thận", "Không đảm bảo hàng"]),
    ("Bạn có thấy sự thay đổi trong chất lượng sản phẩm của Việt Tiến trong thời gian gần đây?", ["Cải thiện đáng kể", "Cải thiện", "Không thay đổi", "Giảm chất lượng", "Không rõ"]),
    ("Bạn có thường xuyên theo dõi các bản tin hoặc cập nhật từ chúng tôi không?", ["Có, tôi luôn cập nhật thông tin mới Email marketing", "Có, nhưng chỉ khi có nội dung thú vị", "Không, tôi không theo dõi", "Tôi chưa từng nhận được bản tin nào"]),
    ("Bạn thích chương trình khuyến mại nào lên tôi?", ["Mua 1 thặng 1", "Giảm giá sản phẩm", "Free ship", "Khác: …………"]),
    ("Bạn có thấy các chương trình khuyến mãi của chúng tôi hấp dẫn không?", ["Có, thường xuyên tham gia", "Có, nhưng hiếm khi tham gia", "Không, tôi không quan tâm", "Không, các chương trình khuyến mãi không đủ hấp dẫn"]),
    ("Bạn thường thấy các quảng cáo của chúng tôi ở đâu nhiều nhất?", ["Facebook", "Instagram", "Tiktok", "Google", "Khác: ………………"]),
    ("Bạn có thấy chúng tôi có các chương trình khuyến mãi và giảm giá phù hợp không?", ["Có, rất phù hợp với nhu cầu của tôi", "Có, nhưng không phải lúc nào cũng phù hợp", "Không, tôi thấy khuyến mãi không hấp dẫn", "Tôi không quan tâm đến khuyến mãi"]),
    ("Những loại nội dung quảng cáo dưới dạng nào thu hút bạn nhất?", ["Video", "Hình ảnh", "Bài viết", "Đánh giá từ khách hàng", "Khác: _______________"]),
    ("Điều gì khiến bạn chọn mua sản phẩm của Việt Tiến vì nhãn hàng khác?", ["Giá rẻ hơn", "Mẫu mã đa dạng hơn", "Chất lượng tốt hơn", "Dịch vụ chăm sóc KH tốt hơn", "Khác:________"]),
    ("Bạn thường mua sắm các sản phẩm quần áo nào ngoài Việt Tiến trong 6 tháng qua?", ["Chanel", "Dior", "Owen", "Routine", "Nhãn hàng khác:_________"]),
    ("Bạn có thấy các chương trình khuyến mãi của các nhãn hàng khác hấp dẫn hơn so với Việt Tiến không?", ["Có, rất hấp dẫn", "Có, một chút", "Không, tương đương", "Không, kém hấp dẫn hơn", "Không theo dõi chương trình khuyến mãi"]),
    ("Bạn cảm nhận thế nào về chất lượng dịch vụ (chăm sóc khách hàng sau và trước bán hàng) của Việt Tiến so với nhãn hàng khác?", ["Tốt hơn", "Tương đương", "Kém hơn", "Không sử dụng dịch vụ hậu mãi"]),
]

# Generate 100 random responses
responses = []
for _ in range(1000):
    response = [random.choice(ans) for q, ans in questions]
    responses.append(response)

# Create DataFrame
df = pd.DataFrame(responses, columns=[q[0] for q in questions])

# Save to CSV
df.to_csv("vi_tien_survey_responses.csv", index=False)
