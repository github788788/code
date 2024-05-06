exec(open('util.py').read())
def upd2(inp):
	cwd = os.getcwd()
	qui = 0
	sta = 0
	bac = ""
	las = 0
	while(qui<1):
		loc = cwd.find("\\",sta)
		print (loc)
		if loc<0:
			bac = cwd[0:las]+"\\"
			break
		sta = loc+1
		las = loc
	print (bac)
	return (bac)
	#rev = cwd[::-1]
		
inp = []
upd2(inp)