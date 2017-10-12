import pandas_datareader as getData
import datetime
import requests_cache
import matplotlib.pyplot as plt
import numpy as np

##here is some code to cache our queries using a sql database, so as to not fck with the API /get banned/get slowed down data. session
##parameter is implemented for all data calls
expire_after = datetime.timedelta(days=3)
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)

##how to collect data, w some modification
##aapl = pdr.get_data_google('AAPL',start=datetime.datetime(2017, 9, 1),end=datetime.datetime(2017,9,28), session = session)
##aapl['diff']= aapl.Open - aapl.Close

##alternative method to retrieve data
##aapl = pdr.DataReader("AAPL", "google",start=datetime.datetime(2017, 9, 27),end=datetime.datetime(2017, 9, 1), session = session)
aapl = getData.DataReader("AAPL", "google", start="2017/9/1", end="2017/9/20")
aapl['diff']= aapl.Open - aapl.Close

print(aapl.tail(5))

##here is some code to bring financial data to a CSV file, for further manipulation
aapl.tail(5).to_csv('aapl.csv')
##aapl.to_csv('/Users/jbrocato/Desktop/stocks/aapl.csv.txt')
##aapl['Adj Close'].to_csv('/Users/jbrocato/Desktop/stocks/aapl.csv.txt',  index=True, sep=',', na_rep='', float_format=None, header=False, index_label=None, mode='w', encoding=None, date_format=None, decimal='.')

import pandas_datareader.data as getData
import datetime

ticker = 'MSFT'
begdate = datetime.datetime(2017,1,2)
enddate = datetime.datetime(2017,1,10)
a = getData.DataReader(ticker, 'google',begdate, enddate)
print(a.head())

print(getData.get_data_google('JPM').head())