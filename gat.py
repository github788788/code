exec(open('util.py').read())
def gat(inp):
	get =str(input("1 for nav to page, blank for no = "))
	if get=="1":
		url = []
		url.append("https://www.thegatewaypundit.com/")
		num([url])
	get =str(input("1 for get data?, blank for no = "))
	fil = "gat.txt"
	if get=="1":
		hod3(["ctrl","a",1,1])
		hod3(["ctrl","c",1,1])
		sw("wordpad.exe",1)
		hod3(["ctrl","v",1,1])
		hod3(["ctrl","s",1,1])
		wri(fil,2)
		key([["enter",1,1,2]])	
		key([["y",2,2,0]])
		gen([tim3,fil])
		af4(1,1)
		sw(fil,1)
	tex = rea([fil])
	ray = []
	end = 0
	beg = 0
	ide = "Comments"
	inc = -1
	while(end<1):
		inc = inc+1
		if inc==0:
			fin = tex.find(ide)
			app1 = tex[fin-300:fin]
			ide2 = "FEATURED\n"
			app2 = app1[app1.find(ide2)+len(ide2):len(app1)]
			ide3 = app2.find("\n")
			app3 = app2[0:ide3]
			app = app3
			print(inc,app)
			ray.append(app)
			continue
		fin2 = tex.find(ide,fin+1)
		if fin2<0:
			break
		app1 = tex[fin-1:fin2]
		print("------------")
		#print(app1)
		app2 = app1[0:app1.find("\n\n")]
		app3 = app2.replace(ide,"")
		app4 = app3.replace("\n"," ")
		app = app4
		ray.append(app)
		fin = fin2+1
	pri(ray)
	tex2 = ""
	for a,val in enumerate(ray):
		tex2 = tex2+"extra extra read all about it headline "
		tex2 = tex2+str(a+1)+" "+val+"\n"
	pri(ray)
	print("yee")
	out = "gat2.txt"
	wri2([out,tex2])
	sw(out,1)


inp = []
gat(inp)