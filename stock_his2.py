exec(open('util.py').read())
def stock_his2(inp):

	import requests
	import numpy as np
	from datetime import datetime
	# if len override_price>0, then price overrides
	symbol =str(input("symbol = "))
	#move_week = int(str(input("move week = ")))
	#override_price = "20"
	override_price =str(input("override_price = "))
	symbol = symbol.upper()
	#symbol = "AMD"
	#override_price = "20"
	#symbol = "SPY"
	#start_date = "2024-01-26"
	#start_date = "2024-02-01"
	#start_date = "2024-02-08"
	#start_date = "2024-02-16"
	#start_date = "2024-02-23"
	#start_date = "2024-03-01"
	start_date = "2023-12-08"
	end_date = start_date
	start_date_object = datetime.strptime(start_date,'%Y-%m-%d')
	import datetime
	#if len(move_week)>0:
	#	start_date_delta = start_date_object-datetime.timedelta(7*move_week)
	#start_date_converted = start_date_delta.strftime('%Y-%m-%d')
	#print(start_date_converted)
	#start_date = start_date_converted
	#sye()
	from datetime import datetime
	#sye()
	#end_date = start_date_converted
	#end_date = "2024-02-23"
	folder = os.getcwd()
	earn_folder = folder+"\\earn\\"
	earn_list = os.listdir(earn_folder)
	file_name = symbol+"."+start_date+".json"
	save_file = earn_folder+file_name
	#print(file_name)
	#sye()
	if file_name not in earn_list:
		#get stock prices
		url1 = "https://api.polygon.io/v2/aggs/ticker/"
		url2 = "/range/1/minute/"
		url3 = "/"
		url4 = "?adjusted=true&sort=asc&limit=500&apiKey=65JaxrhDSYET1StvPxZy1KgpnttWna98"
		url = url1+symbol+url2+start_date+url3+end_date+url4
		#getting data from polygon with json
		polygon_check([])
		data_back = requests.get(url)
		json_data = data_back.json()
		#print("-----------------have done request to polygon--------------------")
		with open(save_file, 'w') as f:
		    json.dump(json_data, f)
		wri2([save_file,json_data])
		print("output file = ",save_file)
		print("have gotten stock data..")
		#sle([5])
	data_dictionary = load_data([save_file])
	#pri(data_dictionary['results'])
	options_data = []
	for a,val in enumerate(data_dictionary['results']):
		more = []
		timestamp_integer = int(val["t"])
		timestamp_integer = (timestamp_integer)/1000
		timestamp_object = datetime.fromtimestamp(timestamp_integer)
		converted_time = timestamp_object.strftime("%m/%d/%Y-%H:%M")
		more.append(converted_time)
		more.append(val["o"])
		more.append(val["h"])
		more.append(val["l"])
		more.append(val["c"])
		options_data.append(more)
	#pri(options_data)
	import pandas as pd
	dataframe = pd.DataFrame(options_data)
	#print(dataframe)
	import plotly.graph_objects as go
	from datetime import datetime
	#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
	print(file_name)
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

	
inp = []
stock_his2(inp)