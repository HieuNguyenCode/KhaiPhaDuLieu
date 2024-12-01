def chukhacnhau(values):
    result = []
    for value1 in values:
        phantudong = set()
        for value2 in values:
            if value1 != value2:
                for SoKyTu in range(1, len(value1) + 1):
                    for layKyTu in range(len(value1) - SoKyTu + 1):
                        value = value1[layKyTu: layKyTu + SoKyTu]
                        if value in value2:
                            phantudong.add(value)

        phantukhacnhau = set()
        for SoKyTu in range(1, len(value1) + 1):
            for layKyTu in range(len(value1) - SoKyTu + 1):
                value = value1[layKyTu: layKyTu + SoKyTu]
                if value not in phantudong:
                    phantukhacnhau.add(value)

        result.append(list(phantukhacnhau))
    return result


def DinhDang(values, cac_ky_tu_duoc_phep):
    khacnhau = chukhacnhau(cac_ky_tu_duoc_phep)

    def process_value(value):
        value = str(value)
        if value == 'nan':
            return ''
        for i in range(len(khacnhau)):
            for j in range(len(khacnhau[i])):
                if khacnhau[i][j] in value:
                    value = cac_ky_tu_duoc_phep[i]
                    break
        return value

    return values.apply(process_value)
