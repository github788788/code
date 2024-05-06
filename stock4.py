#exec(open('util.py').read())

from tkinter import *
from datetime import datetime
import pandas as pd
import tkinter as tk
import os,json,datetime

#sye()
#polygon_check()
#wri2()
#load_data()

def load_data(inp):
	#data = load_data([load_file])
	load_file = inp[0]
	#loaded_data
	loaded_data = ""
	if ".xls" in load_file:
		import xlrd
		workbook = xlrd.open_workbook(load_file)
		sheet1 = workbook.sheet_by_index(0)	
		new_data = []
		for rowNumber in range(sheet1.nrows):
		    row = sheet1.row_values(rowNumber)
		    check = row[::-1]
		    new_row = []
		    for a,val in enumerate(check):
		    	if len(val)==0:
		    		continue
		    	new_row.append(val)
		    new_row = new_row[::-1]
		    new_data.append(new_row)
		    #pri(row)
		    #print(row)
		    #loaded_data.append(row)
		loaded_data = new_data
		#pri(loaded_data)
	if ".csv" in load_file:
		loaded_data = []
		with open(load_file, newline='') as csvfile:
			#make dat.csv in the ear folder, not in the cod folder
		    reader = csv.reader(csvfile)
		    for row in reader:
		    	loaded_data.append(row)
	if ".json" in load_file:
		with open(load_file, 'r') as f:
			loaded_data = json.load(f)
	if ".txt" in load_file or ".py" in load_file:
		#text = rea5(["aul2","py"])
		#che = "."+typ
		#if che not in nam:
		#	nam = nam+"."+typ
		text = open(load_file, "r")
		loaded_data = text.read()
		#return tex2
		#print(f.read())
	return loaded_data


def wri2(inp):
	#wri2([fil,dat])
	#wri2([fil,ray])
	#wri2([output_file,earnings_dates])
	fil = inp[0]
	out = inp[1]
	#print("wh")
	#print(out)
	#sye()
	typ = str(type(out))
	#print (typ)
	bac = ""
	tex = [".txt",".py",".html"]
	#out = inp[1]
	for a,val in enumerate(tex):
		if val in fil:
			#sav = fil.replace(val,"2"+val)
			new = open(fil,"w")
			new.write(out)
			new.close()
			break
	if ".xls" in fil:
		to_write = inp[1]
		#import xlwt
		#from xlwt import Workbook
		new_xls = Workbook()
		add_worksheet = new_xls.add_sheet('Sheet1')
		#writing to worksheet
		for a,val in enumerate(to_write):
			for b,valb in enumerate(val):
				valb = str(valb)
				add_worksheet.write(a,b,valb)
		#column width adjustment
		widths = []
		max_rows = 0
		for a,val in enumerate(to_write):
			check = len(val)
			if check>max_rows:
				max_rows=check
		for a in range(0,max_rows):
			widths.append(0)
		for a,val in enumerate(to_write):
			for b,valb in enumerate(val):
				check = len(str(valb))
				if check>widths[b]:
					widths[b] = check
		#print(widths)
		for a,val in enumerate(widths):
			specific_column = add_worksheet.col(a)
			#column_width.width = (256*check)*2
			specific_column.width = (280*val)
		new_xls.save(fil)
	if ".csv" in fil: 
		"""
		out2 = []
		for a,val in enumerate(out):
			if type(val)==str:
				out2.append([val])
		out = out2
		"""
		if "DataFrame" in typ:
			out.to_csv(fil)  
		if "DataFrame" not in typ:
			#ray = inp[1]
			try:
				csv_file = open(fil, 'wb')
				csv_file.write(out)
				csv_file.close()
			except:
				print("writing .csv failed")
				print("type of data was = "+str(type(fil)))
				#override =str(input("click to continue anyway?"))
	


def polygon_check(inp):
	#polygon_check([])
	file = "polygon.txt"
	text = load_data([file])
	times = nex4([text,"\n","\n"])
	for a,val in enumerate(times):
		times[a] = val.replace("\n","")
	#pri(times)
	from datetime import datetime
	current_time = datetime.now()
	import datetime
	one_min_ago = current_time+datetime.timedelta(seconds=-65)
	print("one min ago",one_min_ago)
	last_minute = 0
	print_last_five =0
	for a,val in enumerate(times):
		try:
			specific = datetime.datetime.strptime(val,"%H:%M:%S - %m/%d/%Y")
		except:
			continue
		if print_last_five<6:
			print("specific" ,specific)
		print_last_five = print_last_five+1
		if specific>one_min_ago:
			last_minute = last_minute+1
			if last_minute==5:
				print("too many requests..must wait..")
	print("last minute = ",last_minute)
	print(str(last_minute)+" requests last minute")
	append_time = current_time.strftime("%H:%M:%S - %m/%d/%Y")
	#current_time = datetime.now()
	text = append_time+"\n"+text
	#print(text)
	#print(current_time)
	wri2([file,text])	



def sye():
	sys.exit()

from tkinter import *
import os
#def stock_polygon(inp):
def stock_polygon():
	import requests
	import numpy as np
	from datetime import datetime
	# if len override_price>0, then price overrides	
	symbol = entry_symbol.get()
	date_in_question = entry_start_date.get()
	#end_date_prelim = entry_end_date.get()
	#change it so that it gets the input information from the input box?
	#trading_data = inp
	#symbol = trading_data[0]
	#date_in_question = trading_data[1]
	#end_prices= date_in_question
	end_prices= entry_end_date.get()
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

#def option_polygon(inp):
def option_polygon():
	import requests
	import numpy as np
	from datetime import datetime
	"""
	trading_data = inp
	symbol = trading_data[0]
	date_in_question = trading_data[1]
	call_or_put = trading_data[2]
	override_expiration = trading_data[3]
	"""
	symbol = entry_symbol.get()
	date_in_question = entry_start_date.get()
	call_or_put = entry_call_or_put.get()
	override_expiration = entry_override_expiration.get()

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
		sye()
		#getting data from polygon with json
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

#def option_yahoo(inp):
def option_yahoo():
	#trading_data = inp
	symbol = entry_symbol.get()
	date_in_question = entry_start_date.get()
	call_or_put = entry_call_or_put.get()
	override_expiration = entry_override_expiration.get()
	"""
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
#interface used to run it..
import tkinter
import tkinter as tk
gui = Tk()
gui.title("get stock info")
gui.geometry("250x300")
def run_option_polygon():
	#symbol = entry_symbol
	##print(symbol)
	print (type(entry_symbol))
	symbol = entry_symbol.get()
	date_in_question = entry_start_date.get()
	call_or_put = entry_call_or_put.get()
	override_expiration = entry_override_expiration.get()
	inputs = [symbol,date_in_question,call_or_put,override_expiration]
	option_polygon()
def run_stock_polygon():
	#symbol = entry_symbol
	##print(symbol)
	
	#symbol = entry_symbol.get()
	#date_in_question = entry_start_date.get()
	inputs = [symbol,date_in_question]
	stock_polygon(inputs)
def run_option_yahoo():
	symbol = entry_symbol.get()
	date_in_question = entry_start_date.get()
	call_or_put = entry_call_or_put.get()
	override_expiration = entry_override_expiration.get()
	inputs = [symbol,date_in_question,call_or_put,override_expiration]
	option_yahoo()

array = []
array.append(["Symbol"])
array.append(["Start Date"])
array.append(["End Date"])
array.append(["Call or Put"])
array.append(["Options Expiration"])
for a,val in enumerate(array):
	Label(gui, text=val[0]).grid(row=a)
row = -1
entry_symbol = Entry(gui)
row = row+1
entry_symbol.grid(row=row,column=1)
entry_symbol.insert(0,"SPY")
entry_start_date = Entry(gui)
row = row+1
entry_start_date.grid(row=row,column=1)
entry_start_date.insert(0,"2024-03-11")
entry_end_date = Entry(gui)
row = row+1
entry_end_date.grid(row=row,column=1)
entry_end_date.insert(0,"2024-03-11")
entry_call_or_put = Entry(gui)
row = row+1
entry_call_or_put.grid(row=row,column=1)
entry_call_or_put.insert(0,"c")
entry_override_expiration = Entry(gui)
row = row+1
entry_override_expiration.grid(row=row,column=1)
entry_override_expiration.insert(0,"515")
button_option_polygon = Button(gui,text ="Polygon Option",command = run_option_polygon)
row = row+1
button_option_polygon.grid(row=row,column=0)
button_option_yahoo = Button(gui,text ="Yahoo Option",command = run_option_yahoo)
button_option_yahoo.grid(row=row,column=1)
button_stock_polygon = Button(gui,text ="Polygon Stock",command = stock_polygon)
row = row+1
button_stock_polygon.grid(row=row,column=0)
def rumble():
	url = "https://rumble.com/c/BannonsWarRoom"
	command = "start \"\" "+url
	os.system(command)
def gmail():
	url = "https://gmail.com"
	command = "start \"\" "+url
	os.system(command)
def trading_view():
	url = "https://www.tradingview.com/chart/?symbol=AMEX%3ASPY"
	command = "start \"\" "+url
	os.system(command)
def unusal_whales():
	url = "https://unusualwhales.com/live-options-flow/free"
	command = "start \"\" "+url
	os.system(command)
def radar():
	url = "https://weather.com/weather/radar/interactive/l/Fredericksburg+VA?canonicalCityId=08a051206dd97b486cb0128338def846c6fcec0d29766b8f97755b41321b1215"
	command = "start \"\" "+url
	os.system(command)
url_array = []
url_array.append(["rumble",rumble])
url_array.append(["gmail",gmail])
url_array.append(["trading_view",trading_view])
url_array.append(["unusal whales",unusal_whales])
url_array.append(["radar",radar])
# Iterate over the labels and buttons
for a,val in enumerate(url_array):
	button_name = val[0]
	#url = val[2]
	button = tk.Button(gui, text=button_name,command=val[1])
	row = row+1
	button.grid(row=row,column=0)
	#button.pack()
mainloop()