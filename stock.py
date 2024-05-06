exec(open('util.py').read())
def stock(inputs):
	#trading_data = inputs
	trading_data = inputs[0]
	symbol = trading_data[0][0]
	date_in_question = trading_data[0][1]
	call_or_put = trading_data[0][2]
	override_expiration = trading_data[0][3]
	function_to_run = trading_data[1][0]
	function_to_run = function_to_run.lower()
	def stock_polygon(inputs):
		trading_data = inputs[0]
		symbol = trading_data[0][0]
		date_in_question = trading_data[0][1]
		call_or_put = trading_data[0][2]
		override_expiration = trading_data[0][3]
		import requests
		import numpy as np
		from datetime import datetime
		# if len override_price>0, then price overrides	
		#symbol = entry_symbol.get()
		#date_in_question = entry_start_date.get()
		#end_date_prelim = entry_end_date.get()
		#change it so that it gets the input information from the input box?
		#trading_data = inp
		#symbol = trading_data[0]
		#date_in_question = trading_data[1]
		#end_prices= date_in_question
		#end_prices= entry_end_date.get()
		symbol = symbol.upper()
		folder = os.getcwd()
		earn_folder = folder+"\\earn\\"
		earn_list = os.listdir(earn_folder)
		file_name = symbol+"."+date_in_question+".json"
		save_file = earn_folder+file_name
		if file_name not in earn_list:
			url1 = "https://api.polygon.io/v2/aggs/ticker/"
			url2 = "/range/1/minute/"
			url3 = "/"
			url4 = "?adjusted=true&sort=asc&limit=500&apiKey=65JaxrhDSYET1StvPxZy1KgpnttWna98"
			url = url1+symbol+url2+date_in_question+url3+end_prices+url4
			print(url)
			#sye()
			#getting data from polygon with json
			polygon_check([])
			data_back = requests.get(url)
			json_data = data_back.json()
			with open(save_file, 'w') as f:
			    json.dump(json_data, f)
			wri2([save_file,json_data])
		price_info = load_data([save_file])
		minute_data = price_info["results"]
		skip_early = 0
		converted = []
		for a,val in enumerate(minute_data):
			timestamp_integer = int(val["t"])
			timestamp_integer = (timestamp_integer)/1000
			timestamp_object = datetime.fromtimestamp(timestamp_integer)
			converted_time = timestamp_object.strftime("%m/%d/%Y-%H:%M")
			if "09:30" in converted_time:
				skip_early=1
			if skip_early<1:
				continue
			more = [converted_time,val["o"],val["h"],val["l"],val["c"]]
			converted.append(more)
			if "16:00" in converted_time:
				break
		dataframe = pd.DataFrame(converted)
		import plotly.graph_objects as go
		from datetime import datetime
		fig = go.Figure(data=[go.Candlestick(x=dataframe[0],
						open=dataframe[1],
		                high=dataframe[2],
		                low=dataframe[3],
		                close=dataframe[4])])
		fig.update_layout(
	    title=file_name
	    )
		fig.show()

	def option_polygon(inputs):
		trading_data = inputs[0]
		symbol = trading_data[0][0]
		date_in_question = trading_data[0][1]
		call_or_put = trading_data[0][2]
		override_expiration = trading_data[0][3]


		(open('util.py').read())
		import requests
		import numpy as np
		from datetime import datetime
		"""
		trading_data = inp
		symbol = trading_data[0]
		date_in_question = trading_data[1]
		call_or_put = trading_data[2]
		override_expiration = trading_data[3]
		symbol = entry_symbol.get()
		date_in_question = entry_start_date.get()
		call_or_put = entry_call_or_put.get()
		override_expiration = entry_override_expiration.get()
		"""
		"""	
		trading_data = inputs
		symbol = trading_data[0][0]
		date_in_question = trading_data[0][1]
		call_or_put = trading_data[0][2]
		override_expiration = trading_data[0][3]
		
		symbol = trading_data[0][0]
		call_or_put = trading_data[0][2]
		override_expiration = trading_data[0][3]
		"""

		from datetime import datetime
		date_object = datetime.strptime(date_in_question,'%Y-%m-%d')
		day_of_week = date_object.weekday()
		if day_of_week==4:
			#next_friday = date_in_question
			next_friday = datetime.strptime(date_in_question,'%Y-%m-%d')
		if day_of_week!=4:
			import datetime
			if day_of_week<4:
				next_friday = date_object+datetime.timedelta(4-day_of_week)
			if day_of_week>4:
				next_friday =date_object+datetime.timedelta(11-day_of_week) 
		if len(symbol)==0:
			symbol =str(input("symbol = "))
		move_week = 0
		if len(override_expiration)==0:
			override_expiration =str(input("override_price = "))
		symbol = symbol.upper()
		call_or_put = call_or_put.upper()
		price = override_expiration
		#start_date = "2024-01-26"
		#start_date = "2024-02-01"
		#start_date = "2024-02-08"
		#start_date = "2024-02-16"
		#start_date = "2024-02-23"
		#start_date = "2024-03-01"
		#start_date = "2024-03-08"
		start_date = date_in_question
		from datetime import datetime
		start_date_object = datetime.strptime(start_date,'%Y-%m-%d')
		#start_date_object = start_date
		import datetime
		start_date_delta = start_date_object-datetime.timedelta(7*move_week)
		start_date_converted = start_date_delta.strftime('%Y-%m-%d')
		#print(start_date_converted)
		start_date = start_date_converted
		#sye()
		from datetime import datetime
		#sye()
		end_date = start_date_converted
		#end_date = "2024-02-23"
		folder = os.getcwd()
		earn_folder = folder+"\\earn\\"
		earn_list = os.listdir(earn_folder)
		file_name = symbol+"."+start_date+".json"
		save_file = earn_folder+file_name
		##print(file_name)
		#sye()
		if file_name not in earn_list:
			#get stock prices
			url1 = "https://api.polygon.io/v2/aggs/ticker/"
			url2 = "/range/1/minute/"
			url3 = "/"
			url4 = "?adjusted=true&sort=asc&limit=500&apiKey=65JaxrhDSYET1StvPxZy1KgpnttWna98"
			url = url1+symbol+url2+start_date+url3+end_date+url4
			print(url)
			#sye()
			#getting data from polygon with json
			#import util
			polygon_check([])
			data_back = requests.get(url)
			json_data = data_back.json()
			##print("-----------------have done request to polygon--------------------")
			with open(save_file, 'w') as f:
			    json.dump(json_data, f)
			wri2([save_file,json_data])
			sle([5])
		price_info = load_data([save_file])
		minute_data = price_info["results"]
		if len(str(price))==0:
			price = minute_data[4]["c"]
		print ("price = ",price)
		price2 = round(float(price))
		options_code = str(price2)+"000"
		for a in range(0,8-len(options_code)):
			options_code = "0"+options_code
		options_code =call_or_put+options_code
		url_options1 = "https://api.polygon.io/v2/aggs/ticker/O:"
		#start_date_object = datetime.strptime(start_date,'%Y-%m-%d')
		expiration_year = next_friday.strftime("%y")
		expiration_month = next_friday.strftime("%m")
		expiration_day = next_friday.strftime("%d")
		options_date = expiration_year+expiration_month+expiration_day
		options_code = options_date+options_code
		
		url_options2 = "/range/1/minute/"
		url_options3 = "/"
		url_options4 = "?adjusted=true&sort=asc&limit=500&apiKey=65JaxrhDSYET1StvPxZy1KgpnttWna98"
		url_options = url_options1+symbol+options_code+url_options2+start_date+url_options3+end_date+url_options4
		#getting data from polygon with json
		#print(url_options)
		#print(options_code)
		file_name = symbol+"."+start_date+"."+options_code+".json"
		save_file = earn_folder+file_name
		#print(file_name)
		#print(save_file)
		#sye()
		if file_name not in earn_list:
			polygon_check([])
			data_back = requests.get(url_options)
			json_data = data_back.json()
			##print("-----------------have done request to polygon--------------------")
			with open(save_file, 'w') as f:
			    json.dump(json_data, f)
			#print("output file = ",save_file)
			#print("now gotten options data..")
		data_dictionary = load_data([save_file])
		##pri(data_dictionary['results'])
		options_data = []
		skip_early = 0
		for a,val in enumerate(data_dictionary['results']):
			more = []
			timestamp_integer = int(val["t"])
			timestamp_integer = (timestamp_integer)/1000
			timestamp_object = datetime.fromtimestamp(timestamp_integer)
			converted_time = timestamp_object.strftime("%m/%d/%Y-%H:%M")
			if "09:30" in converted_time:
				skip_early = 1
			#if skip_early==0:
			#	continue
			more.append(converted_time)
			more.append(val["o"])
			more.append(val["h"])
			more.append(val["l"])
			more.append(val["c"])
			options_data.append(more)
			if "16:00" in converted_time:
				break
		#pri(options_data)
		import pandas as pd
		dataframe = pd.DataFrame(options_data)
		##print(dataframe)
		import plotly.graph_objects as go
		from datetime import datetime
		#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/gui/finance-charts-apple.csv')
		#print(file_name)
		#print(dataframe)
		#sye()
		fig = go.Figure(data=[go.Candlestick(x=dataframe[0],
						open=dataframe[1],
		                high=dataframe[2],
		                low=dataframe[3],
		                close=dataframe[4])])
		fig.update_layout(
	    title=file_name
	    )
		fig.show()

	def option_yahoo(inputs):
		trading_data = inputs[0]
		symbol = trading_data[0][0]
		date_in_question = trading_data[0][1]
		call_or_put = trading_data[0][2]
		override_expiration = trading_data[0][3]
	

		#trading_data = inp
		"""
		symbol = entry_symbol.get()
		date_in_question = entry_start_date.get()
		call_or_put = entry_call_or_put.get()
		override_expiration = entry_override_expiration.get()
		symbol = trading_data[0]
		date_in_question = trading_data[1]
		call_or_put = trading_data[2]
		price = trading_data[3]
		"""
		#date_in_question = "2024-03-10"
		call_or_put = call_or_put.upper()
		symbol = symbol.upper()
		import datetime
		date_object = datetime.datetime.strptime(date_in_question,'%Y-%m-%d')	
		from datetime import datetime
		date_object = datetime.strptime(date_in_question,'%Y-%m-%d')
		day_of_week = date_object.weekday()
		if day_of_week==4:
			#next_friday = date_in_question
			#next_friday = datetime.strptime(date_object,'%Y-%m-%d')
			next_friday = date_object
		if day_of_week!=4:
			import datetime
			if day_of_week<4:
				next_friday = date_object+datetime.timedelta(4-day_of_week)
			if day_of_week>4:
				next_friday =date_object+datetime.timedelta(11-day_of_week) 
		expiration_year = next_friday.strftime("%y")
		expiration_month = next_friday.strftime("%m")
		expiration_day = next_friday.strftime("%d")
		url_yahoo_1 = "https://finance.yahoo.com/chart/"
		#url_yahoo_2 = "&ty=oc&ov=chain_strike&s="
		yahoo_price = str(float(override_expiration))
		#SPY240308C00515500
		yahoo_price = yahoo_price.replace(".","")+"00"
		for a in range(0,8-len(yahoo_price)):
			yahoo_price = "0"+yahoo_price
		print(yahoo_price)
		url_yahoo = url_yahoo_1+symbol+expiration_year+expiration_month+expiration_day
		url_yahoo = url_yahoo+call_or_put+yahoo_price
		#urls = [url_finviz,url_yahoo]
		#url = "https://www.tradingview.com/chart/?symbol=AMEX%3ASPY"
		command = "start \"\" "+url_yahoo
		os.system(command)
	#base = []
	if "stock" in function_to_run and "polygon" in function_to_run:
		stock_polygon([trading_data])
	if "option" in function_to_run and "polygon" in function_to_run:
		option_polygon([trading_data])
	if "option" in function_to_run and "yahoo" in function_to_run:
		option_yahoo([trading_data])
	#polygon_check([])
what_to_run = []
what_to_run.append(["msft","2024-03-28","c","420"])
what_to_run.append(["stock polygon"])
print("naw")
#stock([what_to_run])