exec(open('util.py').read())
def medc():
	#"8047866145"

	hod3(["alt","tab",1,1])
	sw("medc.txt",2)
	hod3(["ctrl","a",1,0])
	hod3(["ctrl","c",1,0])
	hod3(["alt","f4",1,0])
	hod3(["ctrl","v",1,1])
	but(["tab","tab","tab","tab","enter"],0,13)
	#but(["enter"],0,13)
	hod3(["shift","tab",1,1])
	but(["enter"],0,1)
	but(["1"],0,5)
	but(["4"],0,5)
	
	med = "350051186011"
	for a in range(0,len(med)):
		spe = med[a]
		but([spe],0,1)	
	time.sleep(10)
	but(["1"],0,0)

	#but(["4"],0,5)


	#but(["enter"],0,0)

	"""
	hod3(["alt","tab",1,1])
	hod3(["alt","tab",1,1])
	hod3(["alt","tab",1,1])
	


	inp = []
	inp.append([but3,[["tab","tab","tab","tab"],0,1]])
	inp.append([but3,[["enter"],0,10]])
	inp.append([hod3,["shift","tab"1,1]])
	inp.append([but3,[["enter"],0,1]])

	

	inp.append([neu3,[url,2,5]])
	inp.append([cf_et3,["user n",1,0]])
	inp.append([usn])
	inp.append([but3,[["tab","tab","tab","tab"],0,1]])
	inp.append([pas])
	inp.append([but3,[["enter"],0,5]])
	inp.append([cf_etst,["mikael"]])
	inp.append([but3,[["tab","tab","tab","enter"],0,0]])

	fof3(inp)
	"""
	
inp = []
medc(inp)