import pandas as pd

df = pd.read_excel("Concatenated_file.xlsx")

ln = df['CONTACTID'].unique()

df.dropna(subset=['CONTACTID'], inplace=True)
df.drop_duplicates(subset=['CONTACTID'], keep='first', inplace=True)

print(ln)
print(df)
df.to_excel("without_duplicates.xlsx", index=False)
