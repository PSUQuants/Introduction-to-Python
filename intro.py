import pandas_datareader as getData
import datetime

##gets the data using pandas module, and stores it in the dataframe object "ge"
ge = getData.get_data_google('GE',start=datetime.datetime(2017, 9, 1),end=datetime.datetime(2017,10,10))
## creates another column of data in the dataframe, composed of the opening price - the closing price
ge['diff']= ge.Open - ge.Close
##prints your results, the first 5 results specifically. If you want the entire data set, take out "head()"
print(ge.head(5))

#similar method to get data from pandas and store it into the "aapl" dataframe
aapl = getData.DataReader("AAPL", "google", start="2017/9/1", end="2017/9/20")
#manipulates the data, just like above
aapl['diff']= aapl.Open - aapl.Close
#prints results
print(aapl.tail(5))

##another example to get data from pandas and store in the "MSFT" dataframe, using variables in the paramaterization of the dataframe
ticker = 'MSFT'
begdate = datetime.datetime(2017,1,2)
enddate = datetime.datetime(2017,1,10)
a = getData.DataReader(ticker, 'google',begdate, enddate)
print(a.head())

print(getData.get_data_google('JPM').head())