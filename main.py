import re

import numpy as np
import pandas as pd

import DinhDangChu


# Phân tích dữ liệu để đưa ra chiến lược kinh doanh của công ty
# thời trang Việt Tiến

def cot_1(values):
    return values.apply(
        lambda x: 'tùy thuộc vào mức tăng giá' if isinstance(x, float) and str(x) == 'tùy thuộc vào mức tăng giá' else (
            'tùy thuộc vào mức tăng giá' if ' ' in str(x) else ('không' if len(str(x)) > 2 else 'có')
        ))


# chú ý: dấu – khách với dâu -
def cot_2(values):
    def process_value(value):
        value = str(value)
        if value == 'nan':
            return ''
        value = re.sub(r'–', '-', value)
        value = re.sub(r'[a-zA-Z\s]', '', value)

        if len(value) == 5:
            value = value[0:2] + '-' + value[3:5]
        elif len(value) == 4 and not ('-' in value):
            value = value[0:2] + '-' + value[2:4]
        elif len(value) == 3 and not ('-' in value):
            value = value[0:1] + '-' + value[2:3]
        elif len(value) == 2:
            value = value[0:1] + '-' + value[1:2]

        if '-7' in value or '6-' in value:
            value = '6-7'
        elif '-12' in value or '11-' in value:
            value = '11-12'
        elif '-18' in value or '17-' in value:
            value = '17-18'
        elif '-23' in value or '21-' in value:
            value = '21-23'
        elif '11-' in value:
            value = '11-12'
        elif '21-' in value:
            value = '21-23'

        return value

    return values.apply(process_value)


def cot_3(values):
    def process_value(value):
        value = str(value)
        if value == 'nan':
            return ''
        value = re.sub(r'[a-zA-Z\s]', '', value)
        value = re.sub(r'ế', '', value)
        value = re.sub(r'…', '', value)
        value = re.sub(r':', '', value)
        value = re.sub(r'á', '', value)

        if value:
            value = str(int(value) % 8)
            if value == '0':
                value = '8'
        else:
            value = ''

        return value

    return values.apply(process_value)


def cot_4(values, result, check):
    def process_value(value):
        if len(value) != 0 and value not in check:
            value = result

        return value

    return values.apply(process_value)


def cot_5(values):
    def process_value(value):
        if value == '':
            return ''
        if 'bình thường' in value:
            return 'bình thường'
        if 'r' in value or 'ấ' in value or 't' in value:
            if 'k' in value or 'ô' in value or 'n' in value or 'g' in value:
                return 'rất không phù hợp'
            else:
                return 'rất phù hợp'
        else:
            if 'k' in value or 'ô' in value or 'n' in value or 'g' in value:
                return 'không phù hợp'
            else:
                return 'phù hợp'

    return values.apply(process_value)


def cot_6(values):
    def process_value(value):
        value = str(value)
        if value == 'nan':
            return ''
        return value
    return values.apply(process_value)

if __name__ == '__main__':
    df = pd.read_csv("file_nhieu.csv")

    for column in df.columns:
        df[column] = df[column].str.lower()

    # Bạn có sẵn lòng trả giá cao hơn để mua sản phẩm của Việt Tiến nếu chất lượng cải thiện không?
    df["Bạn có sẵn lòng trả giá cao hơn để mua sản phẩm của Việt Tiến nếu chất lượng cải thiện không?"] = cot_1(
        df["Bạn có sẵn lòng trả giá cao hơn để mua sản phẩm của Việt Tiến nếu chất lượng cải thiện không?"])

    # Thời điểm nào trong ngày bạn mua hàng nhiều nhất?
    df["Thời điểm nào trong ngày bạn mua hàng nhiều nhất?"] = cot_2(
        df["Thời điểm nào trong ngày bạn mua hàng nhiều nhất?"])

    df['Thời điểm nào trong ngày bạn mua hàng nhiều nhất?'] = df[
        'Thời điểm nào trong ngày bạn mua hàng nhiều nhất?'].replace(['', None], df[
        'Thời điểm nào trong ngày bạn mua hàng nhiều nhất?'].mode()[0])

    # Bạn quan tâm đến loại sản phẩm nào?
    df["Bạn quan tâm đến loại sản phẩm nào?"] = DinhDangChu.DinhDang(df["Bạn quan tâm đến loại sản phẩm nào?"],
                                                                     ["đồng phục", "thời trang công sở",
                                                                      "phụ kiện thời trang"])

    df['Bạn quan tâm đến loại sản phẩm nào?'] = df[
        'Bạn quan tâm đến loại sản phẩm nào?'].replace(['', None], df[
        'Bạn quan tâm đến loại sản phẩm nào?'].mode()[0])

    # Bạn thường mua sản phẩm ở đâu?
    df['Bạn thường mua sản phẩm ở đâu?'] = DinhDangChu.DinhDang(df['Bạn thường mua sản phẩm ở đâu?'],
                                                                ['facebook', 'tiktok', 'sàn thương mại điện tử',
                                                                 'khác'])
    df['Bạn thường mua sản phẩm ở đâu?'] = df[
        'Bạn thường mua sản phẩm ở đâu?'].replace(['', None], 'khác')

    # Bạn thường dành bao nhiêu thời gian trong ngày để sử dụng mạng xã hội?
    df['Bạn thường dành bao nhiêu thời gian trong ngày để sử dụng mạng xã hội?'] = cot_3(
        df['Bạn thường dành bao nhiêu thời gian trong ngày để sử dụng mạng xã hội?'])

    num_empty = df['Bạn thường dành bao nhiêu thời gian trong ngày để sử dụng mạng xã hội?'].apply(
        lambda x: x == '').sum()

    if num_empty > 0:
        non_empty_values = df['Bạn thường dành bao nhiêu thời gian trong ngày để sử dụng mạng xã hội?'].replace('',
                                                                                                                np.nan).dropna().unique()
        if len(non_empty_values) > 0:
            total_non_empty = len(non_empty_values)
            empty_indices = df[df['Bạn thường dành bao nhiêu thời gian trong ngày để sử dụng mạng xã hội?'] == ''].index
            for idx, empty_idx in enumerate(empty_indices):
                df.at[empty_idx, 'Bạn thường dành bao nhiêu thời gian trong ngày để sử dụng mạng xã hội?'] = \
                    non_empty_values[idx % total_non_empty]

    # Thời gian rảnh bạn thường sử dụng mạng xã hội nào?
    df['Thời gian rảnh bạn thường sử dụng mạng xã hội nào?'] = DinhDangChu.DinhDang(
        df['Thời gian rảnh bạn thường sử dụng mạng xã hội nào?'],
        ['facebook', 'tiktok', 'sàn thương mại điện tử', 'khác'])

    df['Thời gian rảnh bạn thường sử dụng mạng xã hội nào?'] = df[
        'Thời gian rảnh bạn thường sử dụng mạng xã hội nào?'].replace(['', None], 'khác')

    # Bạn thường quan tâm đến sản phẩm nào của Việt Tiến?
    df['Bạn thường quan tâm đến sản phẩm nào của Việt Tiến?'] = DinhDangChu.DinhDang(
        df['Bạn thường quan tâm đến sản phẩm nào của Việt Tiến?'],
        ['ves', 'thời trang công sở', 'phụ kiện (giầy da, thất lưng, ví,…)'])

    df['Bạn thường quan tâm đến sản phẩm nào của Việt Tiến?'] = df[
        'Bạn thường quan tâm đến sản phẩm nào của Việt Tiến?'].replace(['', None], df[
        'Bạn thường quan tâm đến sản phẩm nào của Việt Tiến?'].replace('', None).value_counts().idxmin())

    # Bạn thường mua hàng quan tâm đến điều gì?
    df['Bạn thường mua hàng quan tâm đến điều gì?'] = DinhDangChu.DinhDang(
        df['Bạn thường mua hàng quan tâm đến điều gì?'], ['chất lượng sản phẩm', 'giá thành', 'thương hiệu', 'khác'])

    df['Bạn thường mua hàng quan tâm đến điều gì?'] = df[
        'Bạn thường mua hàng quan tâm đến điều gì?'].replace(['', None],
                                                             df['Bạn thường mua hàng quan tâm đến điều gì?'].replace('',
                                                                                                                     None).value_counts().idxmin())

    # Giá sản phẩm đã tương xứng với chất lượng sản phẩm chưa?
    df['Giá sản phẩm đã tương xứng với chất lượng sản phẩm chưa?'] = DinhDangChu.DinhDang(
        df['Giá sản phẩm đã tương xứng với chất lượng sản phẩm chưa?'],
        ['rất tương xứng', 'tương xứng', 'chưa tương xứng'])

    df['Giá sản phẩm đã tương xứng với chất lượng sản phẩm chưa?'] = cot_4(
        df['Giá sản phẩm đã tương xứng với chất lượng sản phẩm chưa?'], 'tương xứng',
        ['rất tương xứng', 'chưa tương xứng'])

    df['Giá sản phẩm đã tương xứng với chất lượng sản phẩm chưa?'] = df[
        'Giá sản phẩm đã tương xứng với chất lượng sản phẩm chưa?'].replace(['', None],
                                                                            df[
                                                                                'Giá sản phẩm đã tương xứng với chất lượng sản phẩm chưa?'].replace(
                                                                                '',
                                                                                None).value_counts().idxmin())

    # Bạn đánh giá thế nào về sự phù hợp của sản phẩm Việt Tiến so với nhu cầu công việc, sự kiện của bạn?
    df[
        'Bạn đánh giá thế nào về sự phù hợp của sản phẩm Việt Tiến so với nhu cầu công việc, sự kiện của bạn?'] = DinhDangChu.DinhDang(
        df['Bạn đánh giá thế nào về sự phù hợp của sản phẩm Việt Tiến so với nhu cầu công việc, sự kiện của bạn?'],
        ['rất phù hợp', 'phù hợp', 'bình thường', 'không phù hợp', 'rất không phù hợp'])
    df['Bạn đánh giá thế nào về sự phù hợp của sản phẩm Việt Tiến so với nhu cầu công việc, sự kiện của bạn?'] = cot_5(
        df['Bạn đánh giá thế nào về sự phù hợp của sản phẩm Việt Tiến so với nhu cầu công việc, sự kiện của bạn?'])

    df['Bạn đánh giá thế nào về sự phù hợp của sản phẩm Việt Tiến so với nhu cầu công việc, sự kiện của bạn?'] = df[
        'Bạn đánh giá thế nào về sự phù hợp của sản phẩm Việt Tiến so với nhu cầu công việc, sự kiện của bạn?'].replace(
        ['', None],
        df[
            'Bạn đánh giá thế nào về sự phù hợp của sản phẩm Việt Tiến so với nhu cầu công việc, sự kiện của bạn?'].replace(
            '',
            None).value_counts().idxmin())
    # Bạn thấy chất lượng sản phẩm Việt Tiến như thế nào?
    df['Bạn thấy chất lượng sản phẩm Việt Tiến như thế nào?'] = DinhDangChu.DinhDang(
        df['Bạn thấy chất lượng sản phẩm Việt Tiến như thế nào?'], ['rất tốt', 'tốt', 'ổn', 'chưa tốt'])

    df['Bạn thấy chất lượng sản phẩm Việt Tiến như thế nào?'] = df[
        'Bạn thấy chất lượng sản phẩm Việt Tiến như thế nào?'].replace(['', None], df[
        'Bạn thấy chất lượng sản phẩm Việt Tiến như thế nào?'].mode()[0])

    # Đội ngũ tư vấn sản phẩm như thế nào?
    df['Đội ngũ tư vấn sản phẩm như thế nào?'] = DinhDangChu.DinhDang(df['Đội ngũ tư vấn sản phẩm như thế nào?'],
                                                                      ['rất nhiệt tình', 'nhiệt tình', 'thân thiện',
                                                                       'chưa nhiệt tình'])
    df['Đội ngũ tư vấn sản phẩm như thế nào?'] = cot_4(df['Đội ngũ tư vấn sản phẩm như thế nào?'], 'nhiệt tình',
                                                       ['rất nhiệt tình', 'chưa nhiệt tình'])

    df['Đội ngũ tư vấn sản phẩm như thế nào?'] = df['Đội ngũ tư vấn sản phẩm như thế nào?'].replace(['', None], df[
        'Đội ngũ tư vấn sản phẩm như thế nào?'].replace('', None).value_counts().idxmin())

    # Đội ngũ hỗ trợ trả hàng và hỗ trợ khách hàng như thế nào?
    df['Đội ngũ hỗ trợ trả hàng và hỗ trợ khách hàng như thế nào?'] = DinhDangChu.DinhDang(
        df['Đội ngũ hỗ trợ trả hàng và hỗ trợ khách hàng như thế nào?'],
        ['rất nhiệt tình', 'nhiệt tình', 'thân thiện', 'chưa nhiệt tình'])
    df['Đội ngũ hỗ trợ trả hàng và hỗ trợ khách hàng như thế nào?'] = cot_4(
        df['Đội ngũ hỗ trợ trả hàng và hỗ trợ khách hàng như thế nào?'], 'nhiệt tình',
        ['rất nhiệt tình', 'chưa nhiệt tình', 'thân thiện'])

    df['Đội ngũ hỗ trợ trả hàng và hỗ trợ khách hàng như thế nào?'] = df[
        'Đội ngũ hỗ trợ trả hàng và hỗ trợ khách hàng như thế nào?'].replace(
        ['', None],
        df[
            'Đội ngũ hỗ trợ trả hàng và hỗ trợ khách hàng như thế nào?'].replace(
            '',
            None).value_counts().idxmin())

    # Chất lượng giao hàng thế nào?
    df['Chất lượng giao hàng thế nào?'] = DinhDangChu.DinhDang(df['Chất lượng giao hàng thế nào?'],
                                                               ['rất nhanh chóng (từ 2 đến 3 ngày)',
                                                                'nhanh (từ 4 đến 6 ngày)', 'chưa nhanh (trên 7 ngày)'])

    df['Chất lượng giao hàng thế nào?'] = df[
        'Chất lượng giao hàng thế nào?'].replace(
        ['', None],
        df[
            'Chất lượng giao hàng thế nào?'].replace(
            '',
            None).value_counts().idxmin())

    # Chất lượng đóng hàng thế nào?
    df['Chất lượng đóng hàng thế nào?'] = DinhDangChu.DinhDang(df['Chất lượng đóng hàng thế nào?'],
                                                               ['rất cẩn thận', 'cẩn thận', 'chưa cẩn thận',
                                                                'không đảm bảo hàng'])
    df['Chất lượng đóng hàng thế nào?'] = cot_4(df['Chất lượng đóng hàng thế nào?'], 'cẩn thận',
                                                ['rất cẩn thận', 'chưa cẩn thận', 'không đảm bảo hàng'])

    df['Chất lượng đóng hàng thế nào?'] = df[
        'Chất lượng đóng hàng thế nào?'].replace(['', None], df[
        'Chất lượng đóng hàng thế nào?'].mode()[0])

    # Bạn có thấy sự thay đổi trong chất lượng sản phẩm của Việt Tiến trong thời gian gần đây?
    df[
        'Bạn có thấy sự thay đổi trong chất lượng sản phẩm của Việt Tiến trong thời gian gần đây?'] = DinhDangChu.DinhDang(
        df['Bạn có thấy sự thay đổi trong chất lượng sản phẩm của Việt Tiến trong thời gian gần đây?'],
        ['cải thiện đáng kể', 'cải thiện', 'không thay đổi', 'giảm chất lượng', 'không rõ'])
    df['Bạn có thấy sự thay đổi trong chất lượng sản phẩm của Việt Tiến trong thời gian gần đây?'] = cot_4(
        df['Bạn có thấy sự thay đổi trong chất lượng sản phẩm của Việt Tiến trong thời gian gần đây?'], 'cải thiện',
        ['cải thiện đáng kể', 'giảm chất lượng'])

    df['Bạn có thấy sự thay đổi trong chất lượng sản phẩm của Việt Tiến trong thời gian gần đây?'] = df[
        'Bạn có thấy sự thay đổi trong chất lượng sản phẩm của Việt Tiến trong thời gian gần đây?'].replace(
        ['', None],
        df[
            'Bạn có thấy sự thay đổi trong chất lượng sản phẩm của Việt Tiến trong thời gian gần đây?'].replace(
            '',
            None).value_counts().idxmin())

    # Bạn có thường xuyên theo dõi các bản tin hoặc cập nhật từ chúng tôi không?
    df['Bạn có thường xuyên theo dõi các bản tin hoặc cập nhật từ chúng tôi không?'] = DinhDangChu.DinhDang(
        df['Bạn có thường xuyên theo dõi các bản tin hoặc cập nhật từ chúng tôi không?'],
        ['có, tôi luôn cập nhật thông tin mới email marketing', 'có, nhưng chỉ khi có nội dung thú vị',
         'không, tôi không theo dõi', 'tôi chưa từng nhận được bản tin nào'])

    df['Bạn có thường xuyên theo dõi các bản tin hoặc cập nhật từ chúng tôi không?'] = df[
        'Bạn có thường xuyên theo dõi các bản tin hoặc cập nhật từ chúng tôi không?'].replace(
        ['', None],
        df[
            'Bạn có thường xuyên theo dõi các bản tin hoặc cập nhật từ chúng tôi không?'].replace(
            '',
            None).value_counts().idxmin())

    # Bạn thích chương trình khuyến mại nào lên tôi?
    df['Bạn thích chương trình khuyến mại nào lên tôi?'] = DinhDangChu.DinhDang(
        df['Bạn thích chương trình khuyến mại nào lên tôi?'],
        ['mua 1 thặng 1', 'giảm giá sản phẩm', 'free ship', 'khác'])

    df['Bạn thích chương trình khuyến mại nào lên tôi?'] = df[
        'Bạn thích chương trình khuyến mại nào lên tôi?'].replace(
        ['', None],
        df[
            'Bạn thích chương trình khuyến mại nào lên tôi?'].replace(
            '',
            None).value_counts().idxmin())

    # Bạn có thấy các chương trình khuyến mãi của chúng tôi hấp dẫn không?
    df['Bạn có thấy các chương trình khuyến mãi của chúng tôi hấp dẫn không?'] = DinhDangChu.DinhDang(
        df['Bạn có thấy các chương trình khuyến mãi của chúng tôi hấp dẫn không?'],
        ['có, thường xuyên tham gia', 'có, nhưng hiếm khi tham gia', 'không, tôi không quan tâm',
         'không, các chương trình khuyến mãi không đủ hấp dẫn'])

    df['Bạn có thấy các chương trình khuyến mãi của chúng tôi hấp dẫn không?'] = df[
        'Bạn có thấy các chương trình khuyến mãi của chúng tôi hấp dẫn không?'].replace(
        ['', None],
        df[
            'Bạn có thấy các chương trình khuyến mãi của chúng tôi hấp dẫn không?'].replace(
            '',
            None).value_counts().idxmin())

    # Bạn thường thấy các quảng cáo của chúng tôi ở đâu nhiều nhất?
    df['Bạn thường thấy các quảng cáo của chúng tôi ở đâu nhiều nhất?'] = DinhDangChu.DinhDang(
        df['Bạn thường thấy các quảng cáo của chúng tôi ở đâu nhiều nhất?'],
        ['facebook', 'instagram', 'tiktok', 'google', 'khác'])
    df['Bạn thường thấy các quảng cáo của chúng tôi ở đâu nhiều nhất?'] = cot_4(
        df['Bạn thường thấy các quảng cáo của chúng tôi ở đâu nhiều nhất?'], 'khác',
        ['instagram', 'tiktok', 'google', 'facebook'])

    df['Bạn thường thấy các quảng cáo của chúng tôi ở đâu nhiều nhất?'] = df[
        'Bạn thường thấy các quảng cáo của chúng tôi ở đâu nhiều nhất?'].replace(['', None], df[
        'Bạn thường thấy các quảng cáo của chúng tôi ở đâu nhiều nhất?'].mode()[0])

    # Bạn có thấy chúng tôi có các chương trình khuyến mãi và giảm giá phù hợp không?
    df['Bạn có thấy chúng tôi có các chương trình khuyến mãi và giảm giá phù hợp không?'] = DinhDangChu.DinhDang(
        df['Bạn có thấy chúng tôi có các chương trình khuyến mãi và giảm giá phù hợp không?'],
        ['có, rất phù hợp với nhu cầu của tôi', 'có, nhưng không phải lúc nào cũng phù hợp',
         'không, tôi thấy khuyến mãi không hấp dẫn', 'tôi không quan tâm đến khuyến mãi'])

    df['Bạn có thấy chúng tôi có các chương trình khuyến mãi và giảm giá phù hợp không?'] = df[
        'Bạn có thấy chúng tôi có các chương trình khuyến mãi và giảm giá phù hợp không?'].replace(
        ['', None],
        df[
            'Bạn có thấy chúng tôi có các chương trình khuyến mãi và giảm giá phù hợp không?'].replace(
            '',
            None).value_counts().idxmin())

    # Những loại nội dung quảng cáo dưới dạng nào thu hút bạn nhất?
    df['Những loại nội dung quảng cáo dưới dạng nào thu hút bạn nhất?'] = DinhDangChu.DinhDang(
        df['Những loại nội dung quảng cáo dưới dạng nào thu hút bạn nhất?'],
        ['hình ảnh', 'video', 'bài viết', 'khác', 'đánh giá từ khách hàng'])

    df['Những loại nội dung quảng cáo dưới dạng nào thu hút bạn nhất?'] = cot_4(
        df['Những loại nội dung quảng cáo dưới dạng nào thu hút bạn nhất?'], 'khác',
        ['hình ảnh', 'video', 'bài viết', 'đánh giá từ khách hàng'])

    df['Những loại nội dung quảng cáo dưới dạng nào thu hút bạn nhất?'] = df[
        'Những loại nội dung quảng cáo dưới dạng nào thu hút bạn nhất?'].replace(
        ['', None],
        df[
            'Những loại nội dung quảng cáo dưới dạng nào thu hút bạn nhất?'].replace(
            '',
            None).value_counts().idxmin())

    # Điều gì khiến bạn chọn mua sản phẩm của Việt Tiến vì nhãn hàng khác?
    df['Điều gì khiến bạn chọn mua sản phẩm của Việt Tiến vì nhãn hàng khác?'] = DinhDangChu.DinhDang(
        df['Điều gì khiến bạn chọn mua sản phẩm của Việt Tiến vì nhãn hàng khác?'],
        ['chất lượng sản phẩm', 'giá thành', 'thương hiệu', 'khác'])

    df['Điều gì khiến bạn chọn mua sản phẩm của Việt Tiến vì nhãn hàng khác?'] = cot_4(
        df['Điều gì khiến bạn chọn mua sản phẩm của Việt Tiến vì nhãn hàng khác?'], 'khác',
        ['chất lượng sản phẩm', 'giá thành', 'thương hiệu'])

    df['Điều gì khiến bạn chọn mua sản phẩm của Việt Tiến vì nhãn hàng khác?'] = df[
        'Điều gì khiến bạn chọn mua sản phẩm của Việt Tiến vì nhãn hàng khác?'].replace(
        ['', None],
        df[
            'Điều gì khiến bạn chọn mua sản phẩm của Việt Tiến vì nhãn hàng khác?'].replace(
            '',
            None).value_counts().idxmin())

    # Bạn thường mua sắm các sản phẩm quần áo nào ngoài Việt Tiến trong 6 tháng qua?
    df['Bạn thường mua sắm các sản phẩm quần áo nào ngoài Việt Tiến trong 6 tháng qua?'] = DinhDangChu.DinhDang(
        df['Bạn thường mua sắm các sản phẩm quần áo nào ngoài Việt Tiến trong 6 tháng qua?'],
        ["chanel", "dior", "owen", "routine", "nhãn hàng khác"])

    df['Bạn thường mua sắm các sản phẩm quần áo nào ngoài Việt Tiến trong 6 tháng qua?'] = df[
        'Bạn thường mua sắm các sản phẩm quần áo nào ngoài Việt Tiến trong 6 tháng qua?'].replace(
        ['', None],
        df[
            'Bạn thường mua sắm các sản phẩm quần áo nào ngoài Việt Tiến trong 6 tháng qua?'].replace(
            '',
            None).value_counts().idxmin())

    # Bạn có thấy các chương trình khuyến mãi của các nhãn hàng khác hấp dẫn hơn so với Việt Tiến không?
    df[
        'Bạn có thấy các chương trình khuyến mãi của các nhãn hàng khác hấp dẫn hơn so với Việt Tiến không?'] = DinhDangChu.DinhDang(
        df['Bạn có thấy các chương trình khuyến mãi của các nhãn hàng khác hấp dẫn hơn so với Việt Tiến không?'],
        ['có, một chút', 'có, rất hấp dẫn', 'không, tương đương',
         'không, kém hấp dẫn hơn', 'không theo dõi chương trình khuyến mãi'])




    # Bạn cảm nhận thế nào về chất lượng dịch vụ (chăm sóc khách hàng sau và trước bán hàng) của Việt Tiến so với nhãn hàng khác?
    df[
        'Bạn cảm nhận thế nào về chất lượng dịch vụ (chăm sóc khách hàng sau và trước bán hàng) của Việt Tiến so với nhãn hàng khác?'] = cot_6(
        df[
            'Bạn cảm nhận thế nào về chất lượng dịch vụ (chăm sóc khách hàng sau và trước bán hàng) của Việt Tiến so với nhãn hàng khác?'])

    statistics = df.describe(include='all')

    for column in df.select_dtypes(include='object').columns:
        value_counts = df[column].value_counts(normalize=True)
        print(f"Tỷ lệ phần trăm cho cột '{column}':")
        print(value_counts)
    df.to_csv('output.csv', index=False)
