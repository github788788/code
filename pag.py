exec(open('util.py').read())
def pag(inp):
	#n for no ctrl u, y for yes control u
	#pag(["url",5,"n",location])
	url = inp[0]
	wai = inp[1]	
	u = inp[2]
	fil = inp[3]
	num4([[url],wai])
	if "y" in u:
		hod3(["ctrl","u",1,2])
	hod3(["ctrl","a",1,0])
	hod3(["ctrl","c",1,0])
	sw("wordpad.exe",1)
	hod3(["ctrl","v",1,1])
	hod3(["ctrl","s",1,1])
	hod3(["ctrl","a",1,0])
	#loc = "C:\\Users\\-\\0c\\"+out+".txt"
	wri(fil,1)
	key([["enter",2,1,0]])
	af4(1,1)
inp = []
pag(inp)