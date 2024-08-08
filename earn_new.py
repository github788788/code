

exec(open('util.py').read())
import requests
import json
save_folder = "earn\\"
def earnings_dates_polygon(inputs):
	#earnings_dates_polygon([stocks])
	stocks = inputs[0]
	earn_list = os.listdir("earn")
	print(earn_list)
	save_affix = "_earnings_dates_polygon.json"
	to_get = []
	for a,val in enumerate(stocks):
		symbol = val	
		match = symbol+save_affix
		print(match)
		if match in earn_list:
			continue
		else: 
			to_get.append(symbol)
	print(to_get)
	#end()
	for a,val in enumerate(to_get):
		symbol = val	
		url = "https://api.polygon.io/vX/reference/financials?ticker="+symbol+"&limit=50&apiKey=65JaxrhDSYET1StvPxZy1KgpnttWna98"
		response = requests.get(url)
		data = response.json()
		#save_folder = "earn\\"
		save_file = save_folder+symbol+save_affix
		with open(save_file, 'w') as f:
			json.dump(data, f, indent=2)
			print(str(a)+" of "+str(len(to_get)))
			print(f"Data saved to {save_file}")
		if a+1==len(to_get):
			continue
		timer([20])

def historical_prices_yahoo(inputs):
	import yfinance as yf
	stocks = inputs[0]
	earn_list = os.listdir("earn")
	print(earn_list)
	save_affix = "_historical_prices_yahoo.xls"
	to_get = []
	for a,val in enumerate(stocks):
		symbol = val	
		match = symbol+save_affix
		print(match)
		if match in earn_list:
			continue
		else: 
			to_get.append(symbol)
	print(to_get)
	#end()
	for a,val in enumerate(to_get):
		symbol = val	
		stock = yf.Ticker(symbol)
		hist = stock.history(period="5y")
		array = dataframe_to_list2([hist])
		pri(array)
		save_file = save_folder+symbol+save_affix
		print(save_file)
		write_data([save_file,array])
		timer([20])

def gen_market_cap(inputs):
	earn_list = os.listdir("earn")
	list_volume_traded = []
	for a,val in enumerate(earn_list):
		if ".xls" in val:
			print(val)
			file_to_load = save_folder+val
			try:
				historical_prices = load_data([file_to_load])
			except:
				print("file open..close it, moving to next")
				continue
			historical_prices2 = historical_prices[0:2]
			print(historical_prices2)
			open_price = float(historical_prices2[1][1])
			volume = float(historical_prices2[1][5])
			volume_traded = open_price*volume
			symbol = val[0:val.find("_")]
			new_stock = [volume_traded,val]
			list_volume_traded.append(new_stock)
	list_volume_traded.sort(reverse=True)
	pri(list_volume_traded)
	#print(earn_list)

stock_list_length = 50
stocks = load_data(["earn_stocks.xls"])
stocks2 = []
for a,val in enumerate(stocks):
	stocks2.append(val[0])
stocks = stocks2
pri(stocks)
stocks.sort()
for a,val in enumerate(stocks):
	stocks[a]=val.upper()
if stock_list_length>0:
	stocks = stocks[0:stock_list_length]

#earnings_dates_polygon([stocks])
historical_prices_yahoo([stocks])
gen_market_cap([])