import pandas as pd

df = pd.read_csv("C:/Users/user682/PycharmProjects/pythonProject/pokeman/pokemon_data.csv")
# de = pd.read
print(df)
column=list(df)
column[2],column[3] = column[3],column[2]
df.columns=column
print(df)
#or
#df['Type 1'],df['Type 2'] = df['Type 2'],df['Type 1']
#print(df.to_string())
######

new1_df = df.loc[df['Name'].str.startswith('A')]
print(new1_df)

###################
df['oddsum']=df.iloc[1::2,[5,6,9]].sum(axis=1)
print(df)
###########
dates=pd.date_range("20000810",periods=800)
print(dates)
df['#']=dates
print(df)
#or
#df.dates=pd.date_range("20000810",periods=800)
#df.set_index("dates",inplace=true)
#print(df)

df2=df.groupby('Type 1').sum()
print(df2)