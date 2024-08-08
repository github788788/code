exec(open('util.py').read())
exec(open('test.py').read())

import yfinance as yf
stock = yf.Ticker("MSFT")
hist = stock.history(period="5y")

array = dataframe_to_list([hist])
print(array)