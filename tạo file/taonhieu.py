import pandas as pd
import random
import string
import numpy as np

def add_noise_to_string(s, noise_level=0.1):
    noisy_string = list(s)
    num_noisy_chars = int(len(s) * noise_level)
    for _ in range(num_noisy_chars):
        pos = random.randint(0, len(s) - 1)
        noisy_string[pos] = random.choice(string.ascii_letters + string.digits)
    return ''.join(noisy_string)

def randomly_missing_data(column, missing_probability=0.2):
    return column.apply(lambda x: np.nan if random.random() < missing_probability else x)


if __name__ == '__main__':
    df = pd.read_csv("vi_tien_survey_responses.csv")
    for column in df.columns:
        df[column] = df[column].apply(lambda x: add_noise_to_string(str(x), noise_level=0.2))
        # if df[column].dtype == 'object' or df[column].dtype == 'int64' or df[column].dtype == 'float64':
        #     df[column] = randomly_missing_data(df[column], missing_probability=0.3)

    df.to_csv('../file_nhieu.csv', index=False)