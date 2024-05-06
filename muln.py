exec(open('util.py').read())
def muln(ray):

	con = rea4(["muln",'txt'])
	ema = con[0:con.find("\n")]
	ema = frs([ema,",,"])
	#email separator is ",,"
	print (ema)

	tex = ""
	for a,val in enumerate(ema):
		tex = tex+val+"\n"

	print (tex)
	#sys.exit()

	f= open("mule.txt","w")
	f.write(tex)
	f.close() 

	alt(1,1)
	sw("mule.txt",1)
	alt(1,1)
	

	ray = ray
	cor = []
	cor.append(["fir",cf_este3,["new mess",1,0]])
	cor.append(["chr",cf_ee3,["new mess"]])	
	#bro("bro",cor)

	def sam(inp):
		tab = inp[0]
		fun = inp[1]

		#sw(fil,1)
		alt(tab,1)

		#alt(1,1)
		for a,val in enumerate(fun):
			val[0](val[1])
		hod3(["ctrl","c",1,0])
		but(["down","up"],0,0)
		hod3(["alt","tab",1,0])
		hod3(["ctrl","a",1,1])
		hod3(["ctrl","v",1,1])


	sw("muln.txt",1)
	alt(1,1)

	fir = []
	fir.append([hod3,["ctrl","home",1,0]])
	fir.append([key,[["down",1,0,0]]])
	fir.append([hod3,["shift","down",1,0]])

	for a, val in enumerate(ema):	
		cor = []
		cor.append(["fir",cf_este3,["new mess",1,0]])
		cor.append(["chr",cf_ee3,["new mess"]])	
		bro("bro",cor)
		sam([2,[[hod3,["shift","down",1,0]]]])
		key([["enter",1,0,0],["tab",2,0,0]])
		sam([2,fir])
		key([["tab",1,0,0]])
		sam([1,[[htb3,["ctrl","shift","end",1,0]]]])
		cor = []
		cor.append(["fir",cf_este3,["send",1,0]])
		cor.append(["chr",cf_ee3,["send"]])	
		bro("bro",cor)
		if a==len(ema)-1:
			alt(2,1)
			af4(1,1)
			alt(1,1)
			af4(1,1)
inp = []
muln(inp)