exec(open('util.py').read())
def mer2(inp):
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

	pag = []
	pag.append(["0","input","commonhelp homescreen","https://www.commonhelp.virginia.gov/"])
	pag.append(["1","medicaid67","commonhelp login","https://commonhelp.dss.virginia.gov/CASWeb/faces/loginCAS.xhtml?MODULE_NAME=CMB&SERVICE_PROVIDER=COMMON_HELP&LANGUAGE=EN"])
	pag.append(["2","Medmed1!","commonhelp password","https://commonhelp.dss.virginia.gov/CASWeb/faces/loginCASPWD.xhtml"])
	pag.append(["3","","i accept confia agree","https://commonhelp.virginia.gov/access/accessController?id=0.23783123189026012"])
	pag.append(["4","","login home screen","https://commonhelp.virginia.gov/access/accessController?id=0.1560012963127677"])
	pag.append(["5","input","report my change","https://commonhelp.virginia.gov/access/accessController?id=0.919045624613643"])
	pag.append(["6","input",""])
	pag.append(["7","input",""])
	pag.append(["8","input",""])
	pag.append(["9","input",""])
	pag.append(["10","input",""])
	
	dis(pag)

	sta =int(input("page to start on = "))

	def ord(inp):
		inp = inp
	def run0(inp):
		inp = inp
	def run1(inp):
		inp = inp
	def run2(inp):
		inp = inp
	def run3(inp):
		inp = inp
	def run4(inp):
		inp = inp
	def run5(inp):
		inp = inp
	def run6(inp):
		inp = inp
	def run7(inp):
		inp = inp
	def run8(inp):
		inp = inp
	def run9(inp):
		inp = inp

	if sta>0:		
		hod3(["alt","tab",1,1])

	if sta<1:
		num4([url,5])
		hod3(["ctrl","f",1,1])
		wri("changes",1)
		key([["esc",1,0,1],["enter",1,0,5]])
	if sta<2:
		cop([tex,0])
		key([["enter",1,0,5]])
	if sta<3:
		cop([tex,"0c"])
		key([["enter",1,0,5]])
	#hod3(["alt","tab",1,1])
	if sta<4:
		hod3(["ctrl","f",1,1])
		wri("log out",1)
		key([["esc",1,0,1],["tab",1,0,1],["enter",1,0,5]])
	#hod3(["alt","tab",1,0])
	if sta<5:
		hod3(["ctrl","f",1,1])
		wri("report my",1)
		key([["esc",1,0,1],["enter",1,0,5]])
	if sta<6:
		hod3(["ctrl","f",1,1])
		wri("other than",1)
		key([["esc",1,0,1]])
		hod3(["shift","tab",1,1])
		key([["space",1,0,1]])
		nex(ran)
	if sta<7:
		hod3(["ctrl","f",1,1])
		
		#wri("has a new",1)
		wri("Add a new type of income",1)
		key([["esc",1,0,1],["tab",1,0,1],["space",1,0,1]])
		nex(ran)

	hod3(["ctrl","f",1,1])
	wri("another person",1)
	key([["esc",1,0,1]])
	hod3(["shift","tab",1,1])
	key([["space",1,0,1]])
	nex(ran)
	
	cop([tex,"0c"])
	key([["tab",1,0,1]])
	cop([tex,"0c"])
	key([["tab",1,0,1]])
	cop([tex,"0c"])
	key([["tab",1,0,1],["space",1,0,1],["tab",2,0,1],["space",1,0,1],["tab",2,0,1],["space",1,0,1]])
	nex(ran)
	nex(ran)
	nex(ran)
	key([["tab",2,0,1],["space",1,0,1],["tab",2,0,1],["space",1,0,1],["tab",1,0,1]])
	wri("1",1)
	key([["tab",1,0,1],["space",1,0,1],["tab",1,0,1]])
	cop([tex,"0c"])
	key([["tab",2,0,1]])
	cop([tex,"0c"])
	key([["tab",2,0,1]])
	cop([tex,"0c"])
	inp =str(input("submit?  click to finish = "))
	hod3(["alt","tab",1,0])
	nex(ran)

	hod3(["ctrl","f",1,1])
	wri("view and",1)
	key([["esc",1,0,1],["enter",1,0,3]])

	inp =str(input("click when downloaded so can be renamed"))
	#fol = "B:\\Users\\-\\Downloads"
	fol = upd([1])+"Downloads"

	lis = os.listdir(fol)
	old = fol+"\\"+"document.pdf"
	nam = dat.replace("/",".")
	new = fol+"\\"+"med."+nam+".pdf"
	os.rename(old, new)



	#"med.04.03.2022"
	
	
	

	"""
	https://commonhelp.dss.virginia.gov/CASWeb/faces/loginCAS.xhtml?MODULE_NAME=CMB&SERVICE_PROVIDER=COMMON_HELP&LANGUAGE=EN
	medicaid67
	enter
	wait 5(3)
	Medmed1!
	enter
	wait 5
	alt +d
	tab 4x
	enter
	ctrl f, "report my", esc enter
	ctrl f, "other than", esc, shift+tab, space
	ctrl f, "CommonHelp is", esc, shift+tab, enter
	ctrl f, "has a new", esc, tab, space, tabx3, enter
	ctrl f, "another person", esc, shift+tab, space
	ctrl f, "CommonHelp is", esc, shift+tab, enter
	date, "04/03/2022", tab
	amount, "105", tab
	amount, "Family", tab
	tab, space, tabx2, space, tabx2, space
	ctrl f, "CommonHelp is", esc, shift+tab, enter
	ctrl f, "CommonHelp is", esc, shift+tab, enter
	ctrl f, "CommonHelp is", esc, shift+tab, enter
	tabx2, space, tab, space, tab, "1",tab, space, tab,"Mikael",tabx2,"Sandstedt", tabx2,"Medmed1!"
	ctrl f, "CommonHelp is", esc, shift+tab, enter
	ctrl f, "view and", esc, enter
	rename "document" in download dir as.."med.04.03.2022"
	auto email "downloads//med.04.03.2022.pdf" to 4 backup


"""

inp = []
mer2(inp)