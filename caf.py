exec(open('util.py').read())
def caf(inp):

	"""
	hod3(["ctrl","c",1,1])
	key([["esc",1,1,0]])
	sw("wordpad.exe",1)
	hod3(["ctrl","v",1,1])
	hod3(["ctrl","s",1,1])
	wri("E:\\Users\\-\\cod\\caf.txt",2)
	key([["enter",1,1,0]])
	key([["y",1,1,0]])
	key([["enter",1,1,0]])
	hod3(["alt","f4",1,0])
	"""

	tex = rea4(["caf","txt"])
	print(tex)
	las = datetime.datetime.strptime(tex,'%m.%d')
	nex = []
	for a in range(0,3):
		gen = las+datetime.timedelta(a+1)
		gen2 = gen.strftime("%m.%d")
		nex.append(gen2)
	pri(nex)
	



	
	
	
inp = []
caf(inp)