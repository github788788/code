exec(open('util.py').read())
def rt(fi):
	fi =fi+".txt"
	#print "fi",
	fi = open(fi, "r")
	co = fi.read()
	#print co
	return co


inp = []
rt(inp)