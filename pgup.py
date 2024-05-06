exec(open('util.py').read())
def pgup(clicks,wait):
	for a in range(0,clicks):
		hod3(["ctrl","pageup",1,wait])
inp = []
pgup(inp)