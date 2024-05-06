exec(open('util.py').read())
def key2(ray):
	#pop = []
	for a,val in enumerate(ray):
		#try:
		but = []
		print ("val[1]",val[1])
		for b in range(0,val[1]):
			but.append(val[0])
		print (but)
		but3([[but],val[2],val[3]])

inp = []
key2(inp)