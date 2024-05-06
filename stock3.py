exec(open('util.py').read())
#exec(open('stock.py').read())
def stock3(inp):
	#def run_stock():
		#exec(open('stock.py').read())
	what_to_run = []
	what_to_run.append(["msft","2024-03-28","c","420"])
	what_to_run.append(["stock polygon"])
	what_to_generate = []
	what_to_generate.append(["title","stocks"])
	#x axis first, then y axis second
	what_to_generate.append(["geometry","250x300"])
	what_to_generate.append(["entry","symbol","SPY"])
	what_to_generate.append(["entry","start date","2024-03-28"])
	what_to_generate.append(["entry","end date","2024-03-28"])
	what_to_generate.append(["entry","call or put","c"])
	what_to_generate.append(["entry","price","510"])
	#what_to_generate.append(["button","get me my info","stock"])
	#what_to_generate.append(["button","get me my info","lambda: os.system('stock.py')"])
	what_to_generate.append(["button","get me my info","stock(what_to_run)"])
	gen_gui([what_to_generate])
	#stock(what_to_run)

inp = []
stock3(inp)