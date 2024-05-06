exec(open('util.py').read())
def del3(inp):
	
	directory = "C:\\Users\\-\\util\\earn"
	folder_list = os.listdir(directory)
	pri(folder_list)
	for a,val in enumerate(folder_list):
		identifier = "earnings_dates"
		if identifier in val:
			file = directory+"\\"+val
			os.remove(file)
			print(file)

inp = []
del3(inp)