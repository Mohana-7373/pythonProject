import numpy as np
#series
import pandas as pd
a = [1,2,3,4,5,6,7]
series = pd.Series(a)
HAPPY = pd.Series(a, index = [10,20,30,40,50,60,70])
print(HAPPY)
print("\n")

#dataframe = DataFrame
#csv=comma seperated files
df=pd.read_csv('cars.txt')
print(df)
print("\n")
print(df.head(2))
print("\n")

print(df.tail(2))
print("\n")

print(df.info())
print("\n")

print(df.index)
print("\n")
#shows colum values
print(df.columns)
print("\n")

print(df.to_numpy())
print("\n")
#transpose = row2column and colum2row
print(df.T)
print("\n")


s = pd.Series([1,2,3,np.NaN,6,8])
print(s)
print(s[0])
print("\n")

s1 = pd.Series([1,3,5,6,8])
print(s1)
print("\n")

dates = pd.date_range("20130101",periods=6)
print(dates)
print("\n")
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list("ABCD"))
print((df))
print("\n")

df2 = pd.DataFrame(
    {
        "A":1.0,
        "B":pd.Timestamp("20130102"),
        "C":pd.Series(1, index=list(range(4)),dtype="float32"),
        "D":np.array([3]*4,dtype="int32"),
        "E":pd.Categorical(["test","train","test","train"]),
        "F":"foo"
    }
)

print(df2)
print(df2.dtypes)
print("\n")

 # sorting

print( df.sort_index(axis=0, ascending=True))
print("\n")

print( df.sort_values(by="B", ascending=False))
print("\n")
# getting values

print(df["A"])

print("\n")
print(df.A)
print("\n")
print(df.B)
print("\n")
# slicing with data frames

print(df[0:3])
print("\n")

# selection - loc() and at()

print(df.loc[dates[0]])
print("\n")
# multi-axis

print(df.loc[:,["A","B"]])
print("\n")
print(df.loc["20130102":"20130104", ["A", "B"]])
print("\n")
print(df.iloc[3:5, 0:2])
print("\n")
print(df.iloc[[1, 2, 4], [0, 2]])
print("\n")
print(df.iloc[:, 1:3])
print("\n")
# Boolean Indexing

print(df[df["A"] > 0])
print("\n")
print(df[df > 0])
print("\n")
print(df)
print("\n")


# is in
df2 = df.copy()

df2["E"] = ["one", "one", "two", "three", "four", "three"]

df2["F"] = "1.0"
print( df2 )
print("\n")



df2[df2["E"].isin(["two", "four"])]


# automatic alignment

print(df)

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))

print(s1)


df["F"] = s1

print(s1)
print(df)

#Operations

print(df)
print(df.mean())

print (df.mean(1))

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
s
df.sub(s, axis="index")
print(s)

# STRING OPERATIONS

s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
print( s.str.lower())

# concat

df_r = pd.DataFrame(np.random.randn(10, 4))

print(df_r)
print(df_r[:3], df_r[3:7])
print(df_r[7:])

pieces = [df[:3], df[3:7], df[7:]]

pd.concat(pieces)

# join -- works just like sql join

left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})

right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
print(left)
print(right)

pd.merge(left, right, on="key")

# Grouping
# Splitting the data into groups based on some criteria
# Applying a function to each group independently
# Combining the results into a data structure

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

print(df)

df.groupby("A")[["C", "D"]].sum()


print(df.groupby(["A", "B"]).sum())


tuples = list(
    zip(
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    )
)


index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])

df2 = df[:4]

df2

import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)

print(df)

# another complex data
print(pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"]))


# time series

rng = pd.date_range("1/1/2012", periods=100, freq="S")

ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

print(ts)

ts.resample("5Min").sum()


import matplotlib.pyplot as plt

plt.close("all")


ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

ts = ts.cumsum()

print(ts)

ts.plot();


df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)

df = df.cumsum()

print(df)

plt.figure();

df.plot();

plt.legend(loc='best');