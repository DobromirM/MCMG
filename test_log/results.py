import pandas as pd

data_name = "CAL"

df = pd.read_csv(f'./{data_name}_result.csv')

overall = pd.DataFrame([])

for i in range(0, 18):
    overall[df.columns[i][3:]] = (df.iloc[:, i] + df.iloc[:, i + 18])/2

overall.astype(float).round(4).to_csv(f'./{data_name}_full_result.txt', index=True, index_label='index')
