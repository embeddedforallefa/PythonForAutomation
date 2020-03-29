import numpy as np
import pandas as pd

s = pd.Series([1,2,3,4,np.nan,6,8])

print(s)

dates = pd.date_range('20130101', periods=6)

print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list("ABCD"))

print(df)

df2 = pd.DataFrame ({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float'),
                    'D': np.array([3] * 4, dtype = 'int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)

print(df2.dtypes)

print(df2.head())

print(df2.tail(1))

print(df.index)

print(df.columns)

print(df2.to_numpy())

print(df.describe())

print(df.T)

print(df.sort_index(axis=1, ascending=False))
print(df.sort_index(axis=1, ascending=True))

print(df.sort_values(by='B'))

print(df['A'])
print(df[3:])
print(df['20130102':'20130104'])

print(df.loc[dates[0]])

print(df.loc[:,['A', 'B']])

print(df.loc['20130102':'20130104', ['A', 'B']])

print(df.loc['20130102', ['A', 'B']])

print(df.loc[dates[0], 'A'])
print(df.at[dates[0], 'A'])