exec(open('util.py').read())
#exec(open('test.py').read())

stocks = load_data(["earn_stocks.xls"])
stocks2 = []
for a,val in enumerate(stocks):
	stocks2.append(val[0])
stocks = stocks2
pri(stocks)