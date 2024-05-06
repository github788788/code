exec(open('util.py').read())
def aem(ray):
	def pop(con,ide):
		tex = con[0:con.find("\n")]
		qui = 0
		ema = []
		sta = 0
		while(qui<1):
			end = tex.find(ide,sta)
			if end<0:
				end = len(tex)
				qui = 1
			new = tex[sta:end]
			ema.append(new)
			sta = end+len(ide)
		return ema
	con = rea4(["aem",'txt'])
	sui = "\n"
	fir = con.find(sui,0)
	sec = con.find(sui,fir+len(sui))
	ema = pop(con,",,")
	sub = con[fir:sec]
	mes = con[sec+len(sui):len(con)]
	tot = []
	fil = "aem.txt"
	new = ""
	for a,val in enumerate(ema):
		new = new+val+"\n"
	new = new+sub+"\n"
	new = new+mes+"\n"
	def ril():
		key([["right",1,0,0]])
		key([["left",1,0,0]])
		"""	
	def baf(inp):
		bef = inp[0]
		aft = inp[1]
		al1 = inp[2]
		al2 = inp[3]		
		alt(al1,1)
		for a,val in enumerate(bef):
			print ("val",val)
			val[0](val[1])
		hod3(["ctrl","c",1,0])
		ril()
		if al2==0:
			af4(1,1)
		if al2>0:
			alt(al2,1)
		hod3(["ctrl","a",1,0])	
		hod3(["ctrl","v",1,0])
		for a,val in enumerate(aft):
			print("val",val)
			val[0](val[1])
			"""
	alt(1,1)
	var = 0
	ta1 = ""	
	for a, val in enumerate(ema):
		if a==len(ema)-1:
			ta1 = 1
			ta2 = 0
		if a!=len(ema)-1:
			ta1 = 2
			ta2 = 1
		cor = []
		cor.append(["fir",cf_este3,["new mess",1,0]])
		cor.append(["chr",cf_ee3,["new mess"]])	
		bro("bro",cor)
		if a==0:
			sw(fil,1)
			alt(1,1)
		var = cop3([ema,var,2])
		key([["enter",1,0,0]])
		key([["tab",2,0,0]])
		bef = []
		aft = []
		bef.append([hod3,["ctrl","home",1,0]])
		bef.append([key,[["down",1,0,0]]])
		bef.append([hod3,["shift","down",1,0]])
		aft.append([key,[["tab",1,0,0]]])
		bla = [bef,aft,ta1,1]
		baf(bla)
		bef = []
		aft = []
		bef.append([htb3,["ctrl","shift","end",1,0]])
		#ta2 = 1
		if a==len(ema)-1:
			ta2 = 0
		bla = [bef,aft,1,ta2]
		baf(bla)

		cor = []
		cor.append(["fir",cf_este3,["send",1,0]])
		cor.append(["chr",cf_ee3,["send"]])	
		bro("bro",cor)
		
inp = []
aem(inp)