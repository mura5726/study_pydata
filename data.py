url = 'https://vincentarelbundock.github.io/Rdatasets/csv/robustbase/ambientNOxCH.csv'
df_sample = pd.read_csv(url, parse_dates=1, index_col=1)

# dfの準備
df = df_sample.iloc[:, 1:]

# df_monthlyの準備
df_monthly = df.copy()
df_monthly.index = df_monthly.index.map(lambda x: x.month)
df_monthly = df_monthly.groupby(level=0).sum()