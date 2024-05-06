exec(open('util.py').read())
def ban(inp):
	
	wat =str(input("what? 1 for bannon..blank for else.. = "))
	sch([3])
	htb("ctrl","shift","n",1,1)
	alt(1,1)
	af4(1,1)
	out = ""
	if "1" in wat:
		out = "gettr.com/user/warroom/live"
	if wat=="":
		out = "https://gettr.com/livenow"
	wri(out,1)
	key([["enter",1,0,0]])
		

inp = []
ban(inp)