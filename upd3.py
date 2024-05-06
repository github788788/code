exec(open('util.py').read())
def upd3(inp):
	cwd = os.getcwd()
	rev = cwd[::-1]
	fin = rev.find("\\")
	#rev2 = rev[0:fin]
	bac = cwd[0:len(cwd)-fin]
	print (bac)
inp = []
upd3(inp)