import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()

stock = input("Enter a stock ticket symbol: ")
print(stock)

startyear = 2019
startmonth = 1
startday = 1

start = dt.datetime(startyear,startmonth,startday)

now = dt.datetime.now()

df = pdr.get_data_yahoo(stock,start,now)

print(df)

ma = 50

smaString = "sma_"+str(ma)

df[smaString] = df.iloc[:,4].rolling(window=ma).mean()

print(df)

df = df.iloc[ma:]

print(df)

for i in df.index:
    print(i)