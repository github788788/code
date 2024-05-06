exec(open('util.py').read())
def pgd(inp):
	num = inp[0]
	wait = inp[1]
	#for a in range(0,clicks):
	hod3(["ctrl","pagedown",num-1,wait])

inp = []
pgd(inp)