exec(open('util.py').read())
def mul():

	#one_down("alt","tab",1)
	#cf_ests("compose")


	subprocess.Popen(['notepad.exe', "mul.txt"])
	time.sleep(2)
	r3(["right","down"])

	hod3(["ctrl","home",1,0])

	#but(["pageup","pageup"],0,0)
	hod3(["shift","down",1,0])
	hod3(["ctrl","c",1,0])
	but(["right"],0,0)


	subprocess.Popen(['notepad.exe', "mul2.txt"])
	time.sleep(2)
	r3(["right","down"])
	hod3(["ctrl","a",1,0])
	hod3(["ctrl","v",1,0])
	hod3(["ctrl","s",1,0])
	hod3(["alt","f4",1,0])

	ema = []
	con = rt("mul2")
	ide = ","
	cou = con.count(ide)
	beg = 0
	fin = con.find(ide)
	for a in range(0,cou+1):
		fin = con.find(ide,beg)
		if fin<0:
			fin = len(con)
		val = con[beg:fin]
		val = val.replace("\n","")
		ema.append(val)
		beg = fin+1
	print (ema)

	tex = ""

	for a in range(0,len(ema)):
		val = ema[a]
		tex = tex+val+"\n"

	fil2 = "mul3"
	fil2 = fil2+".txt"
	new = open(fil2,"w")
	new.write(tex)
	new.close() 




	#sys.exit()

	hod3(["alt","tab",2,0])

	subprocess.Popen(['notepad.exe', "mul3.txt"])
	time.sleep(1)
	#r2(["right","down"])
	r3(["right","down"])
	hod3(["alt","tab",1,0])
	hod3(["alt","tab",2,0])
	hod3(["alt","tab",1,0])
	

	for a in range(0,len(ema)):

		cf_ests("compose")
		#if a==0:
		hod3(["alt","tab",2,0])
		#if a>0:
		#	hod3(["alt","tab",2,0])
		if a==0:
			hod3(["ctrl","home",1,0])
		hod3(["shift","down",1,0])
		hod3(["ctrl","c",1,0])
		but(["right"],0,0)

		hod3(["alt","tab",1,0])
		hod3(["ctrl","v",1,0])
		but(["tab","tab"],0,0)

		hod3(["alt","tab",2,0])
		#if a==0:
		hod3(["ctrl","home",1,0])
		but(["down"],0,0)

		hod3(["shift","down",1,0])
		hod3(["ctrl","c",1,0])
		but(["right"],0,0)

		hod3(["alt","tab",1,0])
		hod3(["ctrl","v",1,0])
		but(["tab"],0,0)

		hod3(["alt","tab",1,0])
		
		htb("ctrl","shift","end",1,0)
		hod3(["ctrl","c",1,0])
		#hod3(["alt","f4",1,0])
		hod3(["alt","tab",1,0])	

		hod3(["ctrl","a",1,0])
		hod3(["ctrl","v",1,0])

		cf_este2("send",0)
		time.sleep(6)


		
	
		


		
		"""
		but(["tab"],0,0)
		hod3(["alt","tab",1,0])
		
		hod3(["ctrl","home",1,0])
		but(["down"],0,0)
		hod3(["shift","down",1,0])
		hod3(["ctrl","c",1,0])
		but(["right"],0,0)

		hod3(["alt","tab",1,0])
		hod3(["ctrl","v",1,0])
		but(["tab"],0,0)
		

		hod3(["alt","tab",1,0])
		
		htb("ctrl","shift","end",1,0)
		hod3(["ctrl","c",1,0])
		#hod3(["alt","f4",1,0])
		hod3(["alt","tab",1,0])	

		hod3(["ctrl","a",1,0])
		hod3(["ctrl","v",1,0])

		cf_este2("send",0)
		"""
inp = []
mul(inp)