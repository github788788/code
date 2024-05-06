exec(open('util.py').read())
def deg(ray):
	ray = ray
	
	com = []
	com.append("1 for storage, 2 for trash")
	com.append("loops")

	com = fol2(com)

	alt(1,1)

	rig = int(com[0][1])
	loo = int(com[1][1])

	for a in range(0,loo):
		if rig==1:
			tem = "https://drive.google.com/drive/quota"
		if rig==2:
			tem = "https://drive.google.com/drive/trash"
		nu2([[tem],1])
		if rig==1:
			time.sleep(6)
			hod3(["ctrl","a",1,2])
			key([["del",1,0,3]])
		if rig==2:
			time.sleep(5)
			
			cf_etst(["empty"])
			time.sleep(0)
			key([["enter",1,0,2]])
			key([["enter",1,0,0 ]])


	sys.exit()

	com = fol2("1 for storage, 2 for trash")
	com = int(com[0][1])

	url = []
	url.append(tem)

	tem = "https://drive.google.com/drive/quota"
	hod3(["ctrl","a",1,6])
	key([["del",1,0,3]])

	tem = "https://drive.google.com/drive/trash"
	cf_etst(["empty"])
	key([["enter",2,0,0]])

	url.append(tem)
	nu2([url,1])
	inp = []
deg(inp)