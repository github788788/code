exec(open('util.py').read())
def td():
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
	#might have to change timing before ctrl v
	hod3(["alt","f4",1,1])
	hod3(["ctrl","v",1,1])
	but(["tab"],0,0)

	#subprocess.Popen(['notepad.exe', "bac.txt"])
	#sw("td.txt",1)
	loc = "C:\\Users\\-\\Documents\\td.txt"
	sw(loc,1)
	time.sleep(1)
	#r2(["right","down"])
	#r3(["right","down"])
	hod3(["ctrl","home",1,0])
	hod3(["shift","down",1,0])
	hod3(["ctrl","c",1,0])
	one_down("alt","tab",1)
	hod3(["ctrl","v",1,0])
	but(["tab"],0,0)
	one_down("alt","tab",1)
	but(["down"],0,0)
	#one_down("shift","pagedown",1)
	htb("ctrl","shift","end",1,1)
	hod3(["ctrl","c",1,0])
	hod3(["alt","f4",1,1])
	hod3(["ctrl","a",1,0])
	hod3(["ctrl","v",1,0])
	cf_este2("send",0)

	inp = []
td(inp)