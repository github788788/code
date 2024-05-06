exec(open('util.py').read())
def antc(inp):


	hod3(["alt","tab",1,1])
	sw("antc.txt",2)
	hod3(["ctrl","a",1,0])
	hod3(["ctrl","c",1,0])
	hod3(["alt","f4",1,0])
	hod3(["ctrl","v",1,1])
	but(["tab","tab","tab","tab","tab","enter"],0,13)
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

inp = []
antc(inp)