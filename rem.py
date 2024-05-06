exec(open('util.py').read())
def rem(inp):
	
	cwd = os.getcwd()
	fol =cwd+"\\ear" 
	lis = os.listdir(fol)

	for a,val in enumerate(lis):
		if ".csv" in val:
		#if ".xlsx" in val:
			fil = fol+"\\"+val
			print(val)
			print(fil)
			os.remove(fil)

inp = []
rem(inp)