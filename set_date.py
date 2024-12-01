from datetime import datetime
import pandas as pd
import re
current_year = datetime.now().year
current_month = datetime.now().month
def Return(value):
    return pd.to_datetime(value, errors='coerce', dayfirst=False)
def Return_None(value):
    if value:
        return Return(f"{current_year}-{current_month}")
    else:
        return
def min_max(a):
    return 1 <= a <= 12
def mm_yyyy(value, thieunam_mm_yyyy, not_null):
    try:
        if isinstance(value, str) and re.match(r'^\d{4}-\d{2}$', value):
            year, month = value.split('-')
            if 12 >= int(month) >= 1:
                return Return(f"{year}-{month}")
            else:
                return Return_None(not_null)
        elif isinstance(value, str) and re.match(r'^\d{2}-\d{4}$', value):
            month, year = value.split('-')
            if 12 >= int(month) >= 1:
                return Return(f"{year}-{month}")
            else:
                return Return_None(not_null)
        elif isinstance(value, str) and re.match(r'^\d{2}-\d{2}$', value):
            month, year = value.split('-')
            if (min_max(int(month)) or not min_max(int(year))) or (not min_max(int(month)) or min_max(int(year))):
                if 12 >= int(month) >= 1:
                    return Return(f"20{year}-{month}")
                else:
                    return Return(f"20{month}-{year}")
            else:
                return Return_None(not_null)
        elif isinstance(value, str) and re.match(r'^[A-Za-z]+$', value):
            if thieunam_mm_yyyy or not_null:
                return Return(f'{value}-{current_year}')
            else:
                return
        elif isinstance(value, str) and re.match(r'^[A-Za-z]+-\d{2}$', value):
            month, year_suffix = value.split('-')
            full_year = 2000 + int(year_suffix) if int(year_suffix) <= 50 else 1900 + int(year_suffix)
            return Return(f"{month}-{full_year}")
        elif isinstance(value, str) and re.match(r'^[A-Za-z]+-\d{4}$', value):
            month, year = value.split('-')
            return Return(f"{month}-{year}")
        elif isinstance(value, str) and re.match(r'^\d{4}-[A-Za-z]+$', value):
            year, month = value.split('-')
            return Return(f"{month}-{year}")
        return Return_None(not_null)
    except:
        return Return_None(not_null)
def dd_mm_yyyy(value, not_null):
    try:
        if isinstance(value, str) and re.match(r'^\d{2}-\d{2}-\d{2}$', value):
            day, month, year = value.split('-')
            if (12 >= int(month) >= 1) and (31 >= int(day) >= 1):
                return Return(f"20{year}-{month}-{day}")
            elif (12 >= int(day) >= 1) and (31 >= int(month) >= 1):
                return Return(f"20{year}-{day}-{month}")
            else:
                return Return_None(not_null)
        elif isinstance(value, str) and re.match(r'^\d{2}-\d{2}-\d{4}$', value):
            day, month, year = value.split('-')
            if (12 >= int(month) >= 1) and (12 >= int(day) >= 1):
                return Return(f"{year}-{month}-{day}")
            if (12 >= int(month) >= 1) and (31 >= int(day) >= 1):
                return Return(f"{year}-{month}-{day}")
            elif (12 >= int(day) >= 1) and (31 >= int(month) >= 1):
                return Return(f"{year}-{day}-{month}")
            else:
                return Return_None(not_null)
        elif isinstance(value, str) and re.match(r'^\d{2}-\d{4}-\d{2}$', value):
            month, year, day = value.split('-')
            if (12 >= int(month) >= 1) and (12 >= int(day) >= 1):
                return Return(f"{year}-{month}-{day}")
            elif (12 >= int(month) >= 1) and (31 >= int(day) >= 1):
                return Return(f"{year}-{month}-{day}")
            elif (12 >= int(day) >= 1) and (31 >= int(month) >= 1):
                return Return(f"{year}-{day}-{month}")
            else:
                return Return_None(not_null)
        elif isinstance(value, str) and re.match(r'^\d{4}-\d{2}-\d{2}$', value):
            year, month, day = value.split('-')
            if (12 >= int(month) >= 1) and (12 >= int(day) >= 1):
                return Return(f"{year}-{month}-{day}")
            elif (12 >= int(month) >= 1) and (31 >= int(day) >= 1):
                return Return(f"{year}-{month}-{day}")
            elif (12 >= int(day) >= 1) and (31 >= int(month) >= 1):
                return Return(f"{year}-{day}-{month}")
            else:
                return Return_None(not_null)
        elif isinstance(value, str) and re.match(r'^[A-Za-z]+-\d{4}-\d{2}$', value):
            month, year, day = value.split('-')
            if 31 >= int(day) >=1 and 12 >= int(month) >= 1:
                return Return(f"{year}-{month}-{day}")
            elif 31 >= int(day) >=1 and 12 >= int(month) >= 1:
                return Return(f"{year}-{month}-{day}")
            elif 31 >= int(month) >=1 and 12 >= int(day) >= 1:
                return Return(f"{year}-{day}-{month}")
            else:
                return Return_None(not_null)
        elif isinstance(value, str) and re.match(r'^\d{4}-[A-Za-z]+-\d{2}$', value):
            year, month, day = value.split('-')
            if 31 >= int(day) >=1:
                return Return(f"{year}-{month}-{day}")
            else:
                return Return_None(not_null)
        elif isinstance(value, str) and re.match(r'^\d{2}-[A-Za-z]+-\d{4}$', value):
            day, month, year = value.split('-')
            if 31 >= int(day) >=1:
                return Return(f"{year}-{month}-{day}")
            else:
                return Return_None(not_null)
        elif isinstance(value, str) and re.match(r'^[A-Za-z]+-\d{2}-\d{2}$', value):
            month, day, year = value.split('-')
            if 31 >= int(day) >=1:
                return Return(f"{year}-{month}-{day}")
            else:
                return Return_None(not_null)
        return Return_None(not_null)
    except:
        return Return_None(not_null)
def Format_Date(values, thieunam_mm_yyyy=False, not_null=False):
    formatted_values = []
    for i in range(len(values)):
        if pd.isna(values[i]):
            formatted_values.append(Return_None(not_null))
            continue
        date_str1 = values[i].replace("/", "-")
        date_str = date_str1.replace(" ", '-')
        value = date_str.split('-')
        if len(value) == 2 or len(value) == 1:
            formatted_values.append(mm_yyyy(date_str, thieunam_mm_yyyy, not_null))
        elif len(value) == 3:
            formatted_values.append(dd_mm_yyyy(date_str, not_null))
        else:
            formatted_values.append(Return_None(not_null))
    return formatted_values