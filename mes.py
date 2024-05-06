exec(open('util.py').read())
def mes(ray):
	fil = "mes.txt"
	sw(fil,2)
	at(2,1)
	cf_ee("new message")
	at(1,1)
	def cop(bef,aft,var,num):
		#hod3(bef) #["shift","down",1,0]
		bef[0](bef[1])
		hod3(["ctrl","c",1,0])
		but(["right","left"],0,0)
		at(1,1)	
		hod3(["ctrl","a",1,0])
		hod3(["ctrl","v",1,0])
		but3(aft) #but(["tab","tab"],0,0)
		if var==num-1:
			af4(1,1)
		if var<num-1:
			at(1,1)	
	flo = []
	new = []
	new.append([hod3,["shift","down",1,0]])
	new.append([["tab","tab","tab"],0,0])
	flo.append(new)
	new = []
	new.append([hod3,["shift","down",1,0]])
	new.append([["tab"],0,0])
	flo.append(new)
	new = []
	new.append([htb3,["ctrl","shift","end",1,1]])
	new.append([[""],0,0])
	flo.append(new)
	for a,val in enumerate(flo):
		cop(val[0],val[1],a,len(flo))
		inp = []
mes(inp)