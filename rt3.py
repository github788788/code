exec(open('util.py').read())
def rt3(ray):
	fi = ray[0]
	ext = ray[1]
	fi =fi+ext
	#print "fi",
	fi = open(fi, "r")
	co = fi.read()
	#print co
	return co
inp = []
rt3(inp)