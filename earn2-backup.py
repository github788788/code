exec(open('util.py').read())
def earn2(inp):

	date = "2024-03-04"
	list_length = 20

	folder = os.getcwd()
	earn_folder = folder+"\\earn"
	earn_list = os.listdir(earn_folder)
	#pri(earn_list)
	#print(folder)
	#print(earn_folder)
	#sye()
	check_name = "calendar.txt"
	#check = "earn-"+date+".txt"
	save_file = earn_folder+"\\"+"calendar.txt"
	if check_name not in earn_list:
		url = "https://www.investing.com/earnings-calendar/"
		num([url])
		time.sleep(5)
		hod3(["ctrl","end",1,1])
		time.sleep(5)		
		#key([["esc",1,0,1]])
		hod3(["ctrl","a",1,1])
		hod3(["ctrl","c",1,1])
		tex = tki([])
		tex = str(tex)
		save_file = earn_folder+"\\"+"calendar.txt"
		with open(save_file,"w",encoding="utf-8") as f:
		    f.write(tex)
		sw(save_file,2)
		#print(file)
	#print(save_file)
	#sye()
	text = rea5([save_file,"txt"])
	#print(text)
	#sye()
	lines = nex4([text,"\n","\n"])
	lines2 = []
	days_of_week = ["Monday, ","Tuesday, ","Wednesday, ","Thursday, ","Friday, ","Saturday, ","Sunday"]
	skip_if_in = [" ADR"," AG"," Ag"]
	skip_if_not_in = ["(",]
	for a,val in enumerate(lines):
		new = val
		new=new.replace("\n","")
		new=new.replace("\t","")
		#new=new.replace(" ","")
		if len(new)>0:
			skip = 0
			for v,valb in enumerate(days_of_week):
				if valb in new:
					lines2.append(new)
					skip=1
			for v,valb in enumerate(skip_if_in):
				if valb in new:
					skip=1			
			for v,valb in enumerate(skip_if_not_in):
				if valb not in new:	
					skip=1
			if skip==1:
				continue					 
			lines2.append(new)
	lines = lines2
	#pri(lines)
	lines2 = []
	day_of_earnings = ""
	for a,val in enumerate(lines):
		day_passed = 0
		for b,valb in enumerate(days_of_week):
			if valb in val:
				day_of_earnings = []
				day_of_earnings.append(val)
				day_of_earnings = day_of_earnings[0]
				day_of_earnings = day_of_earnings[0:3]+day_of_earnings[day_of_earnings.find(", "):len(day_of_earnings)]
				day_of_earnings = day_of_earnings.replace(day_of_earnings[0:3],str(b+1))
				day_of_earnings = day_of_earnings.replace(", ",",")
				first_comma = day_of_earnings.find(",")
				first_space = day_of_earnings.find(" ",first_comma)
				month = day_of_earnings[first_comma:first_space]
				day_of_earnings = day_of_earnings.replace(month,month[0:4])
				#day_of_earnings = day_of_earnings.replace(month[0:4],str(b+1)+",")
				#list = rep3(stocks,day_replacement_codes)
				from datetime import datetime
				today = datetime.now()
				#date_string = '4,Mar 7,2024'
				date_string = day_of_earnings
				first_comma = date_string.find(",")
				date_string2 = date_string[first_comma+1:len(date_string)]
				#'Mar 7,2024'
				#print(today)
				#print(date_string2)
				date_object = datetime.strptime(date_string2,'%b %d,%Y')
				if today>date_object:
					print("day has passed")
					day_passed=1
				if today<date_object:
					print("day is in the future")
				converted_date = date_object.strftime("%m-%d-%Y")
				converted_date2 = date_string.replace(date_string2,converted_date)
				converted_date = converted_date2
				converted_date = converted_date.replace(",",":")
				day_of_earnings = converted_date
				continue
		if day_passed==1:
			continue
		val = val+"..."
		val = val.replace(" ...","")
		name = val[0:val.find("(")]
		symbol = val[val.find("("):val.find(")")].replace("(","")
		reverse = val[::-1]
		find_space1 = reverse.find(" ")
		find_space2 = reverse.find(" ",find_space1+1)
		market_cap = reverse[0:find_space1][::-1]
		market_cap = abb2([market_cap])
		revenue = reverse[find_space1:find_space2][::-1]
		revenue = abb2([revenue])
		if revenue==0:
			continue
		#print(a,val)
		#print("name",name)
		#print("symbol",symbol)
		#print("market cap", market_cap)
		#print("revenue", revenue)
		add = [market_cap,day_of_earnings,symbol,name,revenue]
		lines2.append(add)
	lines = lines2
	lines.sort(key=lambda x:x[0],reverse=True)
	stock_list = lines[0:list_length]
	#pri(stock_list)
	
	#max 25 a day
	#get previous earnings dates from alphavantage
	import requests
	file_extension = ".json"	
	earn_list = os.listdir(earn_folder)
	key_alpha_vantange = "FK98MBU38O64HAMH"
	for a,val in enumerate(stock_list):
		symbol = val[2]
		check = symbol+"-previous_earnings_dates"
		if check in earn_list:
			continue
		#sym = val.replace(".json","")
		url = "https://www.alphavantage.co/query?function=EARNINGS&symbol="+symbol+ "&apikey="+key_alpha_vantange
		print(symbol,a,val)
		alpha_information = requests.get(url)
		alpha_json = alpha_information.json()
		#sav = dire+"\\"+sym+ext
		save_file = earn_folder+"\\"+check+file_extension
		with open(save_file, 'w') as output_file:
		    json.dump(alpha_json, output_file)
		sle([21])

	#get price history from yfinance
	#max limit?
	import yfinance as yf
	file_extension = ".csv"	
	earn_list = os.listdir(earn_folder)
	for a,val in enumerate(stock_list):
		symbol = val[2]
		check = symbol+"-price_history"
		if check in earn_list:
			continue
		print("missing",end=" ")
		print(symbol,a,val)
		save_file = earn_folder+"\\"+check+file_extension
		print(save_file)
		#continue
		yfinance_information = yf.Ticker(symbol)
		#inc(["yfi"])
		#pro([get,a,sym])
		price_history_5y = yfinance_information.history(period="5y")
		price_history_5y = price_history_5y[::-1]
		#save_file = earn_folder+"\\"+check
		wri2([save_file,price_history_5y])
		sle([21])

	#generate list
	#get previous earnings dates
	#get price history
	#generate previous earnings dates
	#generate price history with earnings dates
	#generate price deltas/deviations over earnings dates?

	"""
	#get_earnings_dates([stock_list])
	#get_price_history([stock_list])
	generate_earnings_dates([stock_list])
	generate_price_history([stock_list])
	get_earnings_dates([stock_list])
	"""



	#MSFT-generated_file
	#earnings list = investing.com
	#alpha vantage?
		

inp = []
earn2(inp)