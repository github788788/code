

exec(open('util.py').read())
import requests
import json
import threading
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
		timer([11])

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
	stocks = inputs[0]
	#stocks = load_data(["earn_volume_traded.xls"])
	pri(stocks)
	final_data = []
	for a,val in enumerate(stocks):
		symbol = val[1]
		try:
			volume_traded = float(val[0])
		except:
			symbol = val
		print(symbol)
		#symbol = val
		load_file = "earn\\"+symbol+"_earnings_dates_polygon.json"
		loaded_data = load_data([load_file])
		quit = 0
		increment = -1
		match = 0
		earnings_dates = []
		hits = 0
		for b in range(0,len(loaded_data['results'])):
			try:
				earnings_date = loaded_data['results'][b]['filing_date']
			except:
				continue
			#print(earnings_date)
			if earnings_date not in earnings_dates:
				earnings_dates.append(earnings_date)
				hits = hits+1
			if hits==10:
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
		for b,valb in enumerate(prices_around_earnings):
			if " " in valb[0]:
				valb[0] = valb[0][0:valb[0].find(" ")]
			if type(valb)==list:
				prices_around_earnings[b]=prices_around_earnings[b][0:6]
			if type(valb)==str:
				prices_around_earnings[b] = [prices_around_earnings[b]]
		already = 0
		counter = 0
		tendencies_gap = []
		tendencies_overday = []
		tendencies_continuance = ""
		for b,valb in enumerate(prices_around_earnings):
			if len(valb)==1:
				counter=0
				already=0
			if counter==1 or counter==2 and already==0:
				#if type(valb)==list:
				if type(valb)==list:
					vol_valb = float(prices_around_earnings[b][5])
					try:
						vol_next = float(prices_around_earnings[b+1][5])
					except:
						continue
					if vol_valb>vol_next:
						#prices_around_earnings[b].append("max")
						already =1
						price_close_day_before = float(prices_around_earnings[b+1][4])
						price_open = float(valb[1])
						price_high = float(valb[2])
						price_low = float(valb[3])
						price_close = float(valb[4])
						change_gap = price_open/price_close_day_before
						change_day = price_close/price_open
						change_gap = dec([ratio_to_percent([change_gap]),2])
						change_day = dec([ratio_to_percent([change_day]),2])
						dec([val,2])
						valb.append(change_gap)
						valb.append(change_day)
						if "-" in str(change_gap) and "-" in str(change_day):
							tendencies_continuance=tendencies_continuance+"C" 
						if "-" not in str(change_gap) and "-" not in str(change_day):
							tendencies_continuance=tendencies_continuance+"C"
						if "-" in str(change_gap) and "-" not in str(change_day):
							tendencies_continuance=tendencies_continuance+"R"
						if "-" not in str(change_gap) and "-" in str(change_day):
							tendencies_continuance=tendencies_continuance+"R"
						tendencies_gap.append(change_gap)
						tendencies_overday.append(change_day)
			counter = counter+1
		print(symbol)
		pri(prices_around_earnings)
		save_file = "earn\\"+symbol+"_prices_around_earnings.xls"
		write_data([save_file,prices_around_earnings])
		print(tendencies_gap)
		print(tendencies_overday)
		print(tendencies_continuance)
		final_data.append([volume_traded,symbol,tendencies_continuance])
	final_data = sorted(final_data, key=lambda x: x[2], reverse=True)
	pri(final_data)
	save_file = "earn_final.xls"
	write_data([save_file,final_data])	
	start_file([save_file,1])



stock_list_length = 500
#stocks_base = load_data(["earn_stocks.xls"])
stocks_base = load_data(["earn_aug_12.xls"])
stocks_base2 = []
for a,val in enumerate(stocks_base):
	stocks_base2.append(val[0])
stocks_base = stocks_base2
stocks_volume_traded = load_data(["earn_volume_traded.xls"])
#pri(stocks)
#stocks.sort()
for a,val in enumerate(stocks_base):
	stocks_base[a]=val.upper()
if stock_list_length>0:
	stocks_base = stocks_base[0:stock_list_length]
	stocks_volume_traded = stocks_volume_traded[0:stock_list_length]

	"""
if __name__ == "__main__":
    threads = []
    for func in [earnings_dates_polygon([stocks_base]), historical_prices_yahoo([stocks_base])]:
        thread = threading.Thread(target=func)
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All tasks are complete")
	"""

    
earnings_dates_polygon([stocks_base])
#historical_prices_yahoo([stocks_base])
gen_volume_traded([stocks_base])
gen_earnings_dates([stocks_base])
