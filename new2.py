exec(open('util.py').read())
def new2(inp):

	#new2([0,["fir","l"]])

	ray = []
	if inp[0]==1:
		#ray = []
		ray.append("bro")
		ray.append("res")
		ray = fol(ray)
	if inp[0]!=1:
		ray = inp[1]
	inp = ray
	print ("inp",inp)
	#sys.exit()
	cor = inp[0]
	com = inp[1]
	fir = []
	fir.append("firefox.lnk")
	fir.append("p")
	fir.append(4)
	goo = []
	goo.append("chrome.lnk")
	goo.append("n")
	goo.append(5)
	ray = []
	ray.append(["fir",fir])
	ray.append(["chr",goo])
	print 
	print ("cor",cor)
	for a,val in enumerate(ray):
		if val[0]==cor:
			"""
			loc = val[1][0]
			key = val[1][1]
			red = val[1][2]
			"""
			ini([1,val[1][0]])
			twd(["ctrl","shift",val[1][1],1,1])
			alt(1,1)
			af4(1,1)		
			res([com,val[1][2]])		
			break
	#sys.exit()
	print ("loc",loc)
	#sys.exit()
	ini([1,loc])
	twd(["ctrl","shift",key,1,1])
	alt(1,1)
	af4(1,1)		
	res([com,red])		


	"""inp = []
new2(inp)