exec(open('util.py').read())
def fof(inp):
	ray = inp
	cop = "cop"
	tex = ""
	for a in range(0,len(ray)):
		val = ray[a][0]
		if val=="cop":
			print (ray[a][1])
			tex = tex+ray[a][1]+"\n"
	new = open("fof.txt","w")
	new.write(tex)
	new.close() 
	mat = 0
	for a in range(0,len(ray)):
		val = ray[a][0]
		if val!="cop":
			ray[a][0](ray[a][1])
		if val=="cop":
			if mat==0:
				subprocess.Popen(['notepad.exe', "fof.txt"])
				time.sleep(1)
				#r2(["right","down"])
				r3(["right","down"])
				but(["pageup","pageup"],0,0)
			if mat>0:
				at(1,1)
			hod3(["shift","down",1,0])
			hod3(["ctrl","c",1,0])
			but(["right"],0,0)
			if a!=len(ray)-2:
				hod3(["alt","tab",1,0])
			if a==len(ray)-2:
				hod3(["alt","f4",1,0])
			#function necesary
			#ray[a][1](ray[a][1])
			hod3(["ctrl","v",1,0])
			mat = mat+1







#exec(open('bas.py').read())inp = []
fof(inp)