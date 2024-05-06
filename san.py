exec(open('util.py').read())
def san(inp):
	inp = inp
	dri = os.getcwd()
	dri = dri[0:dri.find("\\")]
	def sav1():
		shutil.make_archive(dri+"\\Users\\-\\0c", 'zip', dri+"\\Users\\-\\0c")
		cwd = os.getcwd()
		fol = cwd#+"\\0c"
		print (fol)
		fol = dri+"\\Users\\-"
		sw(fol,1)
		hod3(["win","left",1,1])

	def sav4():
		at(1,1)

		cd = os.getcwd()
		du = ud(cd)
		dn = cd.replace(du,"").replace("\\","")
		fl = du+"\\"+dn+".zip"
		
		e = []
		e.append("violin78@protonmail.com")
		e.append("violin78@mail.com")
		e.append("cello34@protonmail.com")
		e.append("usa2@email.com")
		ema = ""
		for a,val in enumerate(e):
			ema = ema+","+val

		tex = []
		tex.append(ema)
		tex.append("0c")
		tex.append(fl)

		cf_este3(["new mess",1,1])


		cop([tex,0])
		#but(["tab","tab","tab"],0,0)
		key([["tab",4,0,0]])
		cop([tex,"0c"])
		htb("ctrl","shift","a",1,1)
		f = []
		f.append(fl)
		for a in range(0,len(f)):
			but(["enter"],2,0)
			cop([tex,"fl"])
			but(["right","enter"],0,5)
		cf_este3(["send",1,1])
		"""

		cor = []
		cor.append(["fir",cf_este3,["send",1,0]])
		cor.append(["chr",cf_ee3,["send"]])	
		bro("bro",cor)
		"""

	inp = []
	print("1 for yes, blank for no")
	inp.append("generate zip?")
	inp.append("email?")	
	inp = inr3(inp)
	gen = inp[0][1]
	bac = inp[1][1]
	print (gen,bac)
	if "1" in gen:
		sav1()
	if "1" in bac:
		sav4()


inp = []
san(inp)