exec(open('util.py').read())
def ke0(ray):
	#pop = []
	for a,val in enumerate(ray):
		#try:
		but = []
		if type(val)==int:
			continue
		for b in range(0,ray[a+1]):
			but.append(val)
		print (but)
		but3([[but],0,0])



#key(["tab",3,"enter",2])
#key([["tab","enter"][2,3]])
inp = []
ke0(inp)