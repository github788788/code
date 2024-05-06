exec(open('util.py').read())
def rtp(fi):
	fi = open(fi+".py", "r")
	co = fi.read()
	#print co
	return co

inp = []
rtp(inp)