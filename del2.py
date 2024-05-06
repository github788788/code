exec(open('util.py').read())
def del2(inp):
	inp = inp
	num =int(input("how many = "))
	hod3(["alt","tab",1,1])
	for a in range(0,num):
		if a==0:
			cfb(["inbox",[["esc",1,0,1],["enter",1,0,1]]])
		if a>0:
			cfb(["new message",[["esc",1,0,1],["tab",1,0,1],["enter",1,0,3]]])
		cfb(["newest",[["esc",1,0,1]]])
		hod3(["shift","tab",4,1])
		key([["enter",1,0,2],["up",2,1,0],["enter",1,0,3],["esc",1,0,1]])
		hod3(["shift","tab",2,1])
		key([["space",1,0,2],["t",1,1,3]])
		cfb(["spam",[["esc",1,0,1],["tab",1,0,1],["enter",1,0,3]]])
		cfb(["newest",[["esc",1,0,1]]])
		hod3(["shift","tab",5,2])
		key([["space",1,0,2]])
		hod3(["ctrl","backspace",1,3])
		key([["tab",1,0,1],["enter",1,0,3]])


inp = []
del2(inp)