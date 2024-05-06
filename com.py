exec(open('util.py').read())
def com(inp):
	#tex = rea4(["goo2","txt"])
	
	sea =str(input("search term = "))
	sea = [sea]
	"""
	#print(tex)
	ide = "\n\n"
	dou = tex.find(ide)
	lis1 = tex[0:dou]
	lis2 = tex[dou:len(tex)]
	lis2 = lis2.replace(ide,"")
	print(lis1,lis2)
	lis3 = nex([lis1,"\n",0])
	lis4 = nex([lis2,"\n",0])
	print(lis3,lis4)
	"""
	url = []
	con = ["facebook","twitter","instagram"]
	#bas = "https://www.google.url/search?q="

	bas = "https://www.google.com/search?client=firefox-b-1-d&q="

	for a,val in enumerate(sea):
		for b,val2 in enumerate(con):
			app = bas+val+" "+val2
			url.append(app)
	pri(url)

	alt(1,1)
	opt2([url,0])


	#num4([url,1])
	
	#opt2([url,1])

	hod3(["ctrl","9",1,1])
	for a in range(0,3):
		hod3(["ctrl","f",1,1])
		#key([["backspace",1,1,1]])
		wri(sea[0],1)
		key([["enter",1,1,0]])
		key([["esc",1,1,0]])
		hod3(["shift","f10",1,0])
		key([["down",1,1,0]])
		key([["enter",1,1,0]])
		hod3(["ctrl","pageup",1,1])

		
	
		
	
	


inp = []
com(inp)

