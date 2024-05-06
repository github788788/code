exec(open('util.py').read())
def cot(inp):
	ray = inp[0]
	tab = inp[1]
	wai = inp[2]
	hod3(["alt","tab",tab,0])


	tex = ""
	for a,val in enumerate(ray):
		tex = tex+val+"\n"

	fil = "cot.txt"
	f= open(fil,"w")
	f.write(tex)
	f.close() 
	
	sw(fil,1)
	for a,val in enumerate(ray):
		hod3(["shift","down",1,0])
		hod3(["ctrl","c",1,0])
		but(["down","up"],0,0)
		if a==len(ray)-1: 
			af4(1,0)
		if a<len(ray)-1: 
			hod3(["alt","tab",1,0])
		hod3(["ctrl","t",1,0])
		hod3(["ctrl","v",1,0])
		key([["enter",1,0,0]])
		if a<len(ray)-1: 
			hod3(["alt","tab",1,0])
	pgu(len(ray),1)		

inp = []
cot(inp)