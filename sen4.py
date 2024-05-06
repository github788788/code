exec(open('util.py').read())
def sen4(inp):
	one_down("alt","tab",1)
	#find_click("new message",0)
	cf_este("new message")
	"""
	but(["tab"],0,0)
	one_down("shift","tab",0)
	but(["space"],0,0)
	"""
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
	#might have to change timing before ctrl v
	hod3(["alt","f4",1,1])
	hod3(["ctrl","v",1,1])
	#but(["tab"],0,0)
	but(["tab","tab","tab"],0,0)
	wri(dn,1)
	but(["tab","tab","tab","tab"],0,1)
	f = []
	#f.append("C:\\Users\\Administrator\\zz-a.rar")
	f.append(fl)
	for a in range(0,len(f)):
		but(["enter"],2,0)
		wri(f[a],1)
		#but(["right","enter"],0,3)
		#but(["enter"],0,3)
		but(["right","enter"],0,3)
	cf_este2("send",0)
inp = []
sen4(inp)