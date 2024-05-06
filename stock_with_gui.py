exec(open('util.py').read())
def stock_with_gui(inp):
	
	what_to_generate = []
	what_to_generate.append(["title","stocks"])
	what_to_generate.append(["geometry","300x300"])
	what_to_generate.append(["entry","symbol"])
	what_to_generate.append(["entry","start date"])
	what_to_generate.append(["entry","end date"])
	what_to_generate.append(["entry","call or put"])
	what_to_generate.append(["entry","price"])

	gen_gui([what_to_generate])

	what_to_run = []
	what_to_run.append(["msft","2024-03-28","c","420"])
	what_to_run.append(["stock polygon"])
	stock2(what_to_run)



inp = []
stock_with_gui(inp)