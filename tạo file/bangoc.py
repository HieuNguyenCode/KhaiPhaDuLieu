import pandas as pd

df = pd.read_csv("vi_tien_survey_responses.csv")

for column in df.columns:
    df[column] = df[column].str.lower()

for column in df.select_dtypes(include='object').columns:
    value_counts = df[column].value_counts(normalize=True)
    print(f"Tỷ lệ phần trăm cho cột '{column}':")
    print(value_counts)
    print()