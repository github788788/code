exec(open('util.py').read())
def opu2(inp):
	url = inp[0]
	tab = inp[1]
	tex = ""
	for a,val in enumerate(url):
		tex = tex+val+"\n"
	print ("tex",tex)
	fil = "opu.txt"
	f=open(fil,"w")
	f.write(tex)
	f.close()
	alt(tab,1)
	sw(fil,1)
	end = len(url)-1
	for a,val in enumerate(url):
		if a==0:	

			hod3(["ctrl","home",1,0])
		if a>0:
			alt(tab,1)
		hod3(["shift","down",1,0])
		hod3(["ctrl","c",1,0])
		key2([["right",1,0,0],["left",1,0,0]])
		if a<end:
			alt(1,0)
		if a==end:
			af4(1,1)
		hod3(["ctrl","t",1,0])
		hod3(["ctrl","v",1,0])
		key2([["enter",1,0,0]])



	

inp = []
opu2(inp)