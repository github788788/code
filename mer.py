exec(open('util.py').read())
def mer(inp):
	inp = inp
	inp = inr3(["month","day","year","amount","giver, 1 if Family"])
	mon = str(inp[0][1])
	if len(mon)==1:
		mon = "0"+mon
	day = str(inp[1][1])
	if len(day)==1:
		day = "0"+day	
	yea = inp[2][1]
	amo = inp[3][1]
	giv = inp[4][1]
	if giv=="1":
		giv = "Family"
	print (giv)
	dat = mon+"/"+day+"/"+yea
	print (inp)
	url = []
	url.append("https://commonhelp.dss.virginia.gov/CASWeb/faces/loginCAS.xhtml?MODULE_NAME=CMB&SERVICE_PROVIDER=COMMON_HELP&LANGUAGE=EN")
	tex = []
	tex.append("medicaid67")
	tex.append("Medmed1!")
	tex.append(dat)
	tex.append(amo)
	tex.append(giv)
	tex.append("Mikael")
	tex.append("Sandstedt")
	tex.append("Medmed1!")
	def nex(inp):
		inp = inp
		hod3(["ctrl","f",1,1])
		wri("CommonHelp is",1)
		key([["esc",1,0,1]])
		hod3(["shift","tab",1,1])
		key([["enter",1,0,5]])
	ran = []
	#dis(pag)
	ray = []
	ray.append([num2,["https://commonhelp.virginia.gov/",1]])
	ray.append([hod3,["ctrl","f",1,1]])
	ray.append([wri3,["changes",1]])
	ray.append([key,[["esc",1,0,1],["enter",1,0,5]]])	
	ray.append([cop,[tex,0]])
	ray.append([key,[["enter",1,0,5]]])
	ray.append([cop,[tex,"0c"]])
	ray.append([key,[["enter",1,0,5]]])
	ray.append([hod3,["ctrl","f",1,1]])
	ray.append([wri3,["log out",1]])
	ray.append([key,[["esc",1,0,1],["tab",1,0,1],["enter",1,0,5]]])
	ray.append([hod3,["ctrl","f",1,1]])
	ray.append([wri3,["report my",1]])
	ray.append([key,[["esc",1,0,1],["enter",1,0,5]]])
	ray.append([hod3,["ctrl","f",1,1]])
	ray.append([wri3,["other than",1]])
	ray.append([key,[["esc",1,0,1]]])
	ray.append([hod3,["shift","tab",1,1]])
	ray.append([key,[["space",1,0,1]]])
	ray.append([nex,ran])
	ray.append([hod3,["ctrl","f",1,1]])	
	ray.append([wri3,["Add a new type of income",1]])
	ray.append([key,[["esc",1,0,1]]])
	ray.append([hod3,["shift","tab",1,1]])	
	ray.append([key,[["space",1,0,1]]])
	#ray.append([key,[["esc",1,0,1],["tab",1,0,1],["space",1,0,1]]])
	ray.append([nex,ran])
	ray.append([hod3,["ctrl","f",1,1]])
	ray.append([wri3,["another person",1]])
	ray.append([key,[["esc",1,0,1]]])
	ray.append([hod3,["shift","tab",1,1]])
	ray.append([key,[["space",1,0,1]]])
	ray.append([nex,ran])
	ray.append([cop,[tex,"0c"]])
	ray.append([key,[["tab",1,0,1]]])
	ray.append([cop,[tex,"0c"]])
	ray.append([key,[["tab",1,0,1]]])
	ray.append([cop,[tex,"0c"]])
	ray.append([key,[["tab",1,0,1],["space",1,0,1],["tab",2,0,1],["space",1,0,1],["tab",2,0,1],["space",1,0,1]]])
	ray.append([nex,ran])
	ray.append([nex,ran])
	ray.append([nex,ran])
	ray.append([key,[["tab",2,0,1],["space",1,0,1],["tab",2,0,1],["space",1,0,1],["tab",1,0,1]]])
	ray.append([wri3,["1",1]])
	ray.append([key,[["tab",1,0,1],["space",1,0,1],["tab",1,0,1]]])
	ray.append([cop,[tex,"0c"]])
	ray.append([key,[["tab",2,0,1]]])
	ray.append([cop,[tex,"0c"]])
	ray.append([key,[["tab",2,0,1]]])
	ray.append([cop,[tex,"0c"]])
	
	#inp =str(input("submit?  click to finish = "))
	
	ray.append([hod3,["alt","tab",1,0]])
	ray.append([nex,ran])
	ray.append([hod3,["ctrl","f",1,1]])
	ray.append([wri3,["view and",1]])
	ray.append([key,[["esc",1,0,1],["enter",1,0,3]]])
	
	#inp =str(input("click when downloaded so can be renamed"))
	
	#print (ray)
	dis(ray)
	#sta = 0
	sta =int(input("sta = ?"))

	if sta>0:
		alt(1,1)
	for a in range(sta,len(ray)):
		val = ray[a]
		val[0](val[1])
	
	fol = upd([1])+"Downloads"
	lis = os.listdir(fol)
	old = fol+"\\"+"document.pdf"
	nam = dat.replace("/",".")
	new = fol+"\\"+"med."+nam+".pdf"
	os.rename(old, new)
inp = []
mer(inp)