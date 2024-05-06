exec(open('util.py').read())
def ema(sub,ray):
	one_down("alt","tab",1)
	find_click("compose",0)
	but(["tab"],0,0)
	one_down("shift","tab",0)
	but(["space"],0,0)
	e = []
	e.append("violin78@protonmail.com")
	e.append("violin78@mail.com")
	e.append("cello34@protonmail.com")
	e.append("usa2@email.com")
	ems = ""
	ray_length = len(e)
	for a in range(0,ray_length):
		ems = ems+e[a]
		if a<ray_length-1:
			ems = ems+", "
	email_file = "em"
	email_file = email_file+".txt"
	f= open(email_file,"w")
	f.write(ems)
	f.close() 
	os.startfile(email_file)
	time.sleep(2)
	hod3(["ctrl","a",1,0])
	hod3(["ctrl","c",1,0])
	hod3(["alt","f4",1,0])
	hod3(["ctrl","v",1,1])
	but(["tab"],0,0)
	wri(sub,1)

	but(["tab","tab"],0,0)
	f = ray
	#f.append(fil)
	for a in range(0,len(f)):
		but(["enter"],2,0)
		wri(f[a],2)
		#but(["right","enter"],0,3)
		but(["enter"],0,3)
	#cf_este("send")
	cf_este2("send",0)
inp = []
ema(inp)

"""
git clone git://gcc.gnu.org/git/gcc.git SomeLocalDir


media788788@gmail.com,desk788788@gmail.com,violin78@protonmail.com,cello34@protonmail.com,violin78@mail.com,usa2@email.com
"""