exec(open('util.py').read())
def ref():

	inp = ["how many"]
	inp = ask(inp)
	num = int(inp[0][1])
	hod3(["alt","tab",1,0])
	for a in range(0,num):
		hod3(["ctrl","r",1,0])
		if a<num-1:
			hod3(["ctrl","pagedown",1,0])
	for a in range(0,num-1):
		hod3(["ctrl","pageup",1,0])

inp = []
ref(inp)