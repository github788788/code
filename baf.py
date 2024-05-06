exec(open('util.py').read())
def baf(inp):
	bef = inp[0]
	aft = inp[1]
	al1 = inp[2]
	al2 = inp[3]		
	alt(al1,1)
	for a,val in enumerate(bef):
		print ("val",val)
		val[0](val[1])
	hod3(["ctrl","c",1,0])
	ril()
	if al2==0:
		af4(1,1)
	if al2>0:
		alt(al2,1)
	hod3(["ctrl","a",1,0])	
	hod3(["ctrl","v",1,0])
	for a,val in enumerate(aft):
		print("val",val)
		val[0](val[1])


inp = []
baf(inp)