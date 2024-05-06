exec(open('util.py').read())
def earn(inp):
	def exit2(inputs):
		#exit2([])
		print("stopping on line "+str(getframeinfo(current).lineno))
		sye()
	current = currentframe()
	list_length = "300"
	#check_name = "2024-03-04"
	#check_name = "2024-03-11"
	#check_name = "2024-03-18"
	#check_name = "2024-03-25"
	#check_name = "2024-04-01"
	#check_name = "2024-04-08"
	#check_name = "2024-04-15"
	#check_name = "2024-04-22"
	check_name = "2024-04-29"
	#check_name = "fortune_"+list_length
	#check_name = "fortune_1000"
	check_extension = ".txt"
	check_file = check_name+check_extension
	folder = os.getcwd()
	earn_folder = folder+"\\earn"
	earn_list = os.listdir(earn_folder)
	save_file = earn_folder+"\\"+check_file
	if check_file not in earn_list:
		import numpy as np 
		import cv2 
		url = "https://www.investing.com/earnings-calendar/"
		#single_url([url,2])
		#num6([url,7,1])
		system_url([url,7])
		#click_logo(["logo_earn.png"])
		logo = "logo_earn.png"
		location = pyautogui.locateOnScreen(logo)	
		#print(location)
		pyautogui.moveTo(location[0],location[1])
		pyautogui.click()

		"""
		screenshot_name = "screenshot.png"
		screenshot_location = earn_folder+"\\"+screenshot_name
		screenshot = pyautogui.screenshot() 
		screenshot = cv2.cvtColor(np.array(screenshot), 
		                     cv2.COLOR_RGB2BGR) 
		cv2.imwrite(screenshot_location, screenshot) 
		logo_name = "logo_earn" 
		#file_name = "logo"
		logo_file =logo_name+".png"
		logo_location = earn_folder+"\\"+logo_file
		#match = logo_name+".png"
		location = pyautogui.locateOnScreen(logo_location)	
		#print(location)
		pyautogui.moveTo(location[0],location[1])
		pyautogui.click()
		"""
		time.sleep(2)
		from datetime import datetime
		start_date_object = datetime.strptime(check_name,'%Y-%m-%d')
		import datetime
		end_date_object = start_date_object+datetime.timedelta(6)
		start_date_string = start_date_object.strftime("%m/%d/%Y")
		end_date_string = end_date_object.strftime("%m/%d/%Y")
		#print(start_date_string,end_date_string)
		pyautogui.keyDown("shift")
		for a in range(0,20):
			pyautogui.press("left")
		pyautogui.keyUp("shift")
		#time.sleep(3)
		#hod3(["ctrl","a",1,2])
		pyautogui.write(start_date_string)
		time.sleep(1)		
		key([["tab",1,0,1]])
		time.sleep(1)		
		pyautogui.write(end_date_string)	
		time.sleep(1)		
		key([["enter",1,0,5]])						
		#time.sleep(1)		
		hod3(["ctrl","end",1,5])
		#time.sleep(5)		
		#key([["esc",1,0,1]])
		hod3(["ctrl","a",1,1])
		hod3(["ctrl","c",1,1])
		tex = tki([])
		tex = str(tex)
		#save_file = earn_folder+"\\"+check_name
		with open(save_file,"w",encoding="utf-8") as f:
		    f.write(tex)
		#sw(save_file,2)
	text = rea5([save_file,"txt"])
	lines = nex4([text,"\n","\n"])
	lines2 = []
	days_of_week = ["Monday, ","Tuesday, ","Wednesday, ","Thursday, ","Friday, ","Saturday, ","Sunday"]
	skip_if_in = [" ADR"," AG"," Ag"]
	skip_if_not_in = ["(",]
	pri(lines)
	for a,val in enumerate(lines):
		val = val.replace("\n","")
		val = val.replace("\t",":")
		if len(val)==0:
			continue
		skip = 0
		for b,valb in enumerate(skip_if_in):
			if valb in val:
				skip = 1	
				break
		end  =0
		for b,valb in enumerate(days_of_week):
			if valb in val:
				lines2.append(val)
				end = 1
		if end==1:
			continue
		for b,valb in enumerate(skip_if_not_in):
			if valb not in val:
				skip = 1	
				break
		if skip==1:
			continue		
		print(a,val,len(val))
		lines2.append(val)
	pri(lines2)
	#exit2([])
	lines3 = []
	day_of_week = "None"
	for a,val in enumerate(lines2):
		skip = 0
		for b,valb in enumerate(days_of_week):
			if valb in val:
				"""
				day_of_week = []
				day_of_week.append(val)
				day_of_week = day_of_week[0]
				"""
				day_of_week = valb
				skip = 1
				break
		if skip==1: 
			continue
		symbol_identifier = "("
		symbol_ender = ")"
		open_parenthesis = val.find(symbol_identifier)
		close_parenthesis = val.find(symbol_ender)
		name = val[0:open_parenthesis]
		symbol = val[open_parenthesis:close_parenthesis]
		symbol = symbol.replace(symbol_identifier,"")
		if len(symbol)==5:
			continue
		reverse = val[::-1]
		start = 0
		quit = 0
		while(quit<1):
			#print("infinite loop wtf")
			if reverse[start]!=":":
				quit = 1
			if reverse[start]==":":
				start = start+1
		reverse = reverse[start:len(reverse)]
		market_cap = reverse[0:reverse.find(":")]
		market_cap = market_cap[::-1]
		if "K" not in market_cap and "M" not in market_cap and "B" not in market_cap:
			continue
		market_cap = multiply_by_10s([market_cap])
		market_cap = int(market_cap)
		if market_cap==0:
			continue
		#val2 = reverse[::-1]
		add = [market_cap]
		add.append(day_of_week.replace(", ",""))
		add = add+[symbol,name]
		#add = [market_cap,symbol,name]
		print (val,start)
		#print(add)
		lines3.append(add)
	lines3.sort(key=lambda x:x[0],reverse=True)
	pri(lines3)
	#exit2([])
	stock_list = lines3
	pri(stock_list)
	#exit2([])
	from datetime import date
	date_gotten = str(date.today()) 
	def yfinance_earnings(inp):
		#get earnings dates and earnings surprise from yfinance
		#yfinance_earnings([stock_list])
		stock_list = inp[0]
		wait_per_request = inp[1]
		import time
		import yfinance as yf
		file_extension = ".csv"	
		earn_list = os.listdir(earn_folder)
		for a,val in enumerate(stock_list):
			symbol = val[2]
			#check = symbol+"-yfinance_earnings"+file_extension
			exists = 0
			for b,valb in enumerate(earn_list):
				if symbol in valb:
					if "yfinance_earnings" in valb:
						info_date = valb[valb.find("--"):valb.find(file_extension)]
						info_date = info_date.replace("--","")
						print(str(a)+","+str(b)+"-""load_file = "+valb)
						print("info_date = "+str(info_date))
						exists = 1
						break
			if exists==1:
				continue
			#if check in earn_list:
			#	continue
			print(a,len(stock_list),symbol)
			#print(earn_folder+"\\"+check)
			time_before = time.time()
			data = yf.Ticker(symbol)
			time_after = time.time()
			request_duration = time_after-time_before
			print ("request duration = ",request_duration)
			try:
				earn = data.earnings_dates
			except KeyboardInterrupt: 
				print("doing keyboard interrupt")
				sye()
			except:
				print (symbol," earnings data failed, moved to next")
				continue
			time_after2 = time.time()
			sorting_duration = time_after2-time_after
			print ("sorting duration = ",sorting_duration)
			save_file = earn_folder+"\\"+symbol+".yfinance_earnings--"+date_gotten+file_extension
			print("save_file = "+save_file)
			#save_file = earn_folder+"\\"+check
			#add date of when got file
			wri2([save_file,earn])
			if a==len(stock_list)-1:
				continue			
			sle([wait_per_request])

	def yfinance_history(inp):
		#get price history from yfinance
		#max limit?
		#yfinance_history([stock_list])
		stock_list = inp[0]
		wait_per_request = inp[1]
		import yfinance as yf
		file_extension = ".csv"	
		earn_list = os.listdir(earn_folder)
		for a,val in enumerate(stock_list):
			symbol = val[2]
			exists = 0
			for b,valb in enumerate(earn_list):
				if symbol in valb:
					if "yfinance_history" in valb:
						info_date = valb[valb.find("--"):valb.find(file_extension)]
						info_date = info_date.replace("--","")
						print(str(a)+","+str(b)+"-""load_file = "+valb)
						print("info_date = "+str(info_date))
						exists = 1
						break
			if exists==1:
				continue
			print(a,len(stock_list),symbol)
			#print(earn_folder+"\\"+check)
			#save_file = earn_folder+"\\"+check
			save_file = earn_folder+"\\"+symbol+".yfinance_history--"+date_gotten+file_extension
			print("save file = "+save_file)
			#add date of when got file
			yfinance_information = yf.Ticker(symbol)
			price_history_5y = yfinance_information.history(period="5y")
			price_history_5y = price_history_5y[::-1]
			
			wri2([save_file,price_history_5y])
			if a==len(stock_list)-1:
				continue			
			sle([wait_per_request])
	#get info from yfinance
	wait_per_request = 11
	yfinance_earnings([stock_list,wait_per_request])
	yfinance_history([stock_list,wait_per_request])
	#sye()
	"""
	generate earnings dates file
	and price history file with
	earings dates
	"""
	counter = 0
	how_many_earnings = 10
	from datetime import datetime
	today = datetime.now()
	file_extension = ".csv"
	earn_folder = folder+"\\earn"
	earn_list = os.listdir(earn_folder)
	for a,val in enumerate(stock_list):
		val[0]=int(val[0])
		symbol = val[2]
		for b,valb in enumerate(earn_list):
			if symbol in valb:
				if "yfinance_earnings" in valb:
					load_file = earn_folder+"\\"+valb
					break
		#load_name = symbol+"-yfinance_earnings"
		#load_file = earn_folder+"\\"+load_name+file_extension
		earnings_dates = load_data([load_file])
		earnings_dates2 = []
		stock_messed_up = 0
		for b in range(1,len(earnings_dates)):
			valb = earnings_dates[b]
			#if b==15:
			#	break
			specific_date = valb[0]
			check = specific_date[0:specific_date.find(" ")]
			#date_object = datetime.strptime(date_string2,'%b %d,%Y')
			try:
				date_object = datetime.strptime(check,'%Y-%m-%d')
			except:
				continue
			difference = today-date_object
			difference = difference.days
			###print(difference)
			###print(date_object)
			if b==1:
				if difference>365:
					stock_messed_up=1
					break
			if date_object>today:
				continue
			if date_object<today:
				##print("check",check)
				##print(earnings_dates2)
				check2 = [check]
				if check2 in earnings_dates2:
					continue
				#earnings_dates2.append([check])
				earnings_dates2.append([str(specific_date)])
				if len(earnings_dates2)==how_many_earnings:
					break
		###pri(earnings_dates2)
		if stock_messed_up==1:
			continue
		####pri(earnings_dates2)	
		earnings_dates = earnings_dates2
		output_extension = ".xls"
		output_file = earn_folder+"\\"+symbol+"-earnings_dates"+output_extension
		#wri2([output_file,earnings_dates])
		#loaded_price_history = 
		#load_file = output_file
		load_extension = ".csv"		
		for b,valb in enumerate(earn_list):
			if symbol in valb:
				if "yfinance_history" in valb:
					load_file = earn_folder+"\\"+valb
					break
		#load_file = earn_folder+"\\"+symbol+"-yfinance_history"+load_extension
		price_history = load_data([load_file])
		prices_around_earnings = []
		prices_around_earnings.append(price_history[0])
		###pri(earnings_dates2)
		for b,valb in enumerate(earnings_dates2):
			date_and_time = []
			date_and_time.append(valb[0])
			date_and_time = date_and_time[0]
			date_and_time = date_and_time.replace(" ","..")
			date_and_time = date_and_time.replace("00:00","0")
			##print(date_and_time)
			#sye()
			valb = valb[0]
			valb = valb[0:valb.find(" ")]
			##print(valb)
			#print (date_and_time)
			for c,valc in enumerate(price_history):
				if valb in valc[0]:
					try:
						check = price_history[c+1]
					except:
						continue
					if "Date" in price_history[c-1]:
						continue
					#prices_around_earnings.append([valb])
					prices_around_earnings.append([date_and_time])
					prices_around_earnings.append(price_history[c-1])
					prices_around_earnings.append(price_history[c])
					prices_around_earnings.append(price_history[c+1])
		###pri(prices_around_earnings)
		for b,valb in enumerate(prices_around_earnings):
			if b==0:
				continue
			if b>0:
				for c,valc in enumerate(valb):
					if c==0:
						continue
					if c>0:
						##print(symbol)
						try:
							valc2 = decimal_places([valc,2])
						except:
							fail = "fail"
						#	###pri(prices_around_earnings)
							#print(symbol)
							###pri(prices_around_earnings)
							#sye()
						prices_around_earnings[b][c]=valc2

		for b,valb in enumerate(prices_around_earnings):
			prices_around_earnings[b] = valb[0:6]	 
		new = []
		for b,valb in enumerate(prices_around_earnings):
			if b==0:
				valb.append("Gap")
				valb.append("High")
				valb.append("Low")
				valb.append("Close")
				new.append(valb)
				continue
			if b>0 and len(valb)>1:
				valb[0] = valb[0][0:valb[0].find(" ")]
				try:
					error = len(prices_around_earnings[b+1])
				except:
					continue
				##print(error)
				if error>1:
					#print("valb",valb)
					try:
						gap = float(valb[1])/float(prices_around_earnings[b+1][4])
					except:
						continue
					gap = convert_to_percent([gap])
					valb.append(gap)
					high = float(valb[2])/float(valb[1])
					high = convert_to_percent([high])
					valb.append(high)
					low = float(valb[3])/float(valb[1])
					low = convert_to_percent([low])
					valb.append(low)
					close = float(valb[4])/float(valb[1])
					close = convert_to_percent([close])
					valb.append(close)
			new.append(valb)
		prices_around_earnings=new
		output_extension = ".xls"
		output_file = earn_folder+"\\"+symbol+"-prices_around_earnings"+output_extension
		wri2([output_file,prices_around_earnings])
		####print(symbol)
	master = []
	for a,val in enumerate(stock_list):
		symbol = val[2]
		file_name = symbol+"-prices_around_earnings.xls"
		load_file = earn_folder+"\\"+file_name
		try:
			data = load_data([load_file])
		except:
			continue
		loaded_data = []
		new_set = []
		for b,valb in enumerate(data):
			if len(valb)==1:
				if len(new_set)>0:
					loaded_data.append(new_set)
				new_set = []
			new_set.append(valb)
		movements = ""
		closes_same_direction = ""
		dollars_traded = 0
		price = 0
		volume = 0
		time_symbol = ""
		for b,valb in enumerate(loaded_data):
			for c,valc in enumerate(valb):
				if c==0:
					specific = valc[0]
					contains = valc[0]
					continue
				check = valc[0]
				analyze = []
				if check in contains:
					#print("check",check)
					#print("contains",contains)
					print(symbol,"contains",valc)
					#continue
					time_find = contains.find("..")
					time_of_day = contains[time_find+2:contains.find(":")]
					time_of_day = int(time_of_day)
					if time_of_day>10:
						correct = valb[c-1]
						time_symbol = "2:"
						#val[1] = val[1].replace(":","2:")
					if time_of_day<10:
						correct = valb[c]
						time_symbol = "1:"
						#stock_list[a][1] = stock_list[a][1].replace(":","2:")
						#val[1] = val[1].replace(":","1:")s
					price= float(correct[4])
					volume= float(correct[5])
					print("volume",volume)
					print("correct",correct)
					print(a,len(stock_list),symbol,price,volume)
					dollars_traded = price*volume
					dollars_traded = int(dollars_traded)
					dollars_traded = dollars_traded/1000000000
					#dollars_traded = dollars_traded/1000000
					#if "e" in str(dollars_traded):
					#	dollars_traded = 0
					print("dollars_traded",dollars_traded)
					dollars_traded = decimal_places([dollars_traded,2])
					print("dollars_traded",dollars_traded)
					gap= correct[6]
					day_up= correct[7]
					day_down= correct[8]
					close= correct[9]
					direction = ""
					if "-" in str(gap):
						if abs(float(day_down))>abs(float(day_up)):
							direction = "C"
						if abs(float(day_down))<abs(float(day_up)):
							direction = "R"
						if "-" in close:
							closes_value = "Y"
						if "-" not in close:
							closes_value = "N"							
					if "-" not in str(gap):
						if abs(float(day_up))>abs(float(day_down)):
							direction = "C"
						if abs(float(day_up))<abs(float(day_down)):
							direction = "R"
						if "-" in close:
							closes_value = "N"
						if "-" not in close:
							closes_value = "Y"							
					closes_same_direction = closes_same_direction+closes_value
					movements = movements+direction
		stock_list[a][1] = stock_list[a][1].replace(":",time_symbol)
		further = []
		further.append(dollars_traded)
		further.append(movements)
		further = further+val
		if len(movements)>0:
			master.append(further)	
	#for a,val in enumerate(stock_list):
	#	val[2] = val[2].replace("2024","24")	
	#master.sort(key=lambda x:x[1],reverse=True)
	#master.sort(key=lambda x:x[0],reverse=True)
	master.sort(reverse=True)
	pri(master)
	final_name = check_name+".xls"
	final_file = earn_folder+"\\"+final_name
	wri2([final_file,master])
	sw2([final_file,0])


	"""
	#intrinio api key?
	#OjA1ZDkxNjNkZGJlODZlZGFlM2UxZTA2NWM1Y2Q5ODBj
		
	#https://financialmodelingprep.com/api/v3/earnings-surprises/PANW?apikey=3g0Q4QqV7Ycs47oWLYo9mS2lkTNUYzlx
	#250 a day
	#apikey=
	#3g0Q4QqV7Ycs47oWLYo9mS2lkTNUYzlx

	import finnhub
	finnhub_client = finnhub.Client(api_key="cd5d3iqad3i5nc8nt3s0cd5d3iqad3i5nc8nt3sg")
	####print(finnhub_client.company_earnings('WBA', limit=5))
	#key = cd5d3iqad3i5nc8nt3s0cd5d3iqad3i5nc8nt3sg
	"""
inp = []
earn(inp)