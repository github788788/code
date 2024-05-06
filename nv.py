exec(open('util.py').read())
def nv(ra,at,ot,wt):
	lt(ra)
	if at==1:
		hod3(["alt","tab",at,0])
	sw("notepad.exe",1)
	#re(0,["left","down"],1)
	#re(0,["right","down"],1)
	#r2(["right","down"])
	hod3(["ctrl","o",1,ot])#2
	na = os.path.basename(__file__)
	na = na.replace(".py","")
	lo = os.getcwd()+"\\"+na
	wri(lo+".txt",wt)#2
	but(["enter"],0,0)
	co = rt(lo)
	le = co.count("\n")
	#print le
	#sys.exit()
	for a in range(0,le):
		#hod3(["shift","end",1,0])
		hod3(["shift","down",1,0])
		hod3(["ctrl","c",1,0])
		but(["down","up"],0,0)
		#but(["left","down"],0,0)		
		hod3(["alt","tab",1,0])
		hod3(["ctrl","t",1,1])
		hod3(["ctrl","v",1,1])
		but(["enter"],0,0)
		hod3(["alt","tab",1,0])
	hod3(["alt","f4",1,0])
inp = []
nv(inp)