

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
	print("toget",to_get)
	for a,val in enumerate(to_get):
		symbol = val	
		print(symbol)
		stock = yf.Ticker(symbol)
		hist = stock.history(period="5y")
		array = dataframe_to_list2([hist])
		array.append(array[0])
		array = array[1:len(array)]
		array = array[::-1]

		pri(array)
		print(symbol)
		save_file = save_folder+symbol+save_affix
		print(save_file)
		write_data([save_file,array])
		timer([20])

def gen_volume_traded(inputs):
	import json
	stock_list = inputs[0]
	earn_list = os.listdir("earn")
	load_affix = "_historical_prices_yahoo.xls"
	list_volume_traded = []
	for a,val in enumerate(stock_list):
		file_to_load = save_folder+val+load_affix
		print(a,len(stock_list),file_to_load)
		try:
			historical_prices = load_data([file_to_load])
		except:
			continue
		historical_prices2 = historical_prices[0:2]
		try:
			open_price = float(historical_prices2[1][1])
		except:
			continue
		volume = float(historical_prices2[1][5])
		volume_traded = open_price*volume
		volume_traded = volume_traded/1000000
		volume_traded = dec([volume_traded,2])
		symbol = val[0:val.find("_")]
		load_file = "earn\\"+val+"_earnings_dates_polygon.json"
		with open(load_file, 'r') as file:
		    data = json.load(file)
		    #print(data['results'])
		    #print(data)
		    #print(data.keys())
		    try:
		    	company = data['results'][0]['company_name']
		    except:
		    	continue
		    new_stock = [volume_traded,val,company]
		list_volume_traded.append(new_stock)
	list_volume_traded.sort(reverse=True)
	pri(list_volume_traded)
	save_file = "earn_volume_traded.xls"
	try:
		write_data([save_file,list_volume_traded])
	except:
		#close file that is open 
		meow = "meow"
	start_file([save_file,1])
	#print(earn_list)

def gen_earnings_dates(inputs):
	#stock_list = inputs[0]
	stocks = load_data(["earn_volume_traded.xls"])
	pri(stocks)
	for a,val in enumerate(stocks):
		symbol = val[1]
		#load_affix = "_earnings_dates_polygon.json"
		#load_file = "earn\\"+symbol+load_affix
		#loaded_info = load_data([load_file])
		load_file = "earn\\"+symbol+"_earnings_dates_polygon.json"
		loaded_data = load_data([load_file])
		#print(loaded_data)
		quit = 0
		increment = -1
		match = 0
		earnings_dates = []
		while(quit<1):
			increment = increment+1
		#for b in range(0,10):
			try:
				earnings_date = loaded_data['results'][increment]['filing_date']
			except:
				continue
				"""
			year_or_quarter = loaded_data['results'][increment]['timeframe']
			if "quarterly" not in year_or_quarter:
				continue
				"""
			if earnings_date not in earnings_dates:
				earnings_dates.append(earnings_date)
				match = match+1
				if match==10:
					break
		print(symbol)
		pri(earnings_dates)
		historical_prices = load_data(["earn\\"+symbol+"_historical_prices_yahoo.xls"])
		prices_around_earnings = []
		for b,valb in enumerate(earnings_dates):
			new = []
			for c,valc in enumerate(historical_prices):
				if valb in valc[0]:
					prices_around_earnings.append(valb)
					prices_around_earnings.append(historical_prices[c-1])	
					prices_around_earnings.append(historical_prices[c])
					prices_around_earnings.append(historical_prices[c+1])
			#pri(new)
			#prices_around_earnings.append(new)
		for b,valb in enumerate(prices_around_earnings):
			if " " in valb[0]:
				valb[0] = valb[0][0:valb[0].find(" ")]
			if type(valb)==list:
				prices_around_earnings[b]=prices_around_earnings[b][0:6]
			scan = 1
			if scan==1:
				if type(valb)==list:
					print(valb)
					vol_day_after = float(valb[5])
					vol_day_of = float(prices_around_earnings[b+1][5])
					print(vol_day_after,vol_day_of)
					scan=0
			if type(valb)==str:
				scan=1
		#pri(prices_around_earnings)



stock_list_length = 500
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
#gen_volume_traded([stocks])
gen_earnings_dates([stocks])