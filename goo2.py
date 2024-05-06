exec(open('util.py').read())
def goo2(inp):

	sea = whi2(["sea"])
	print(sea)
	sye()
	
	tex = rea4(["goo2","txt"])

	ide = "\n\n"
	dou = tex.find(ide)
	lis1 = tex[0:dou]
	lis2 = tex[dou:len(tex)]
	lis2 = lis2.replace(ide,"")
	print(lis1,lis2)
	lis3 = nex([lis1,"\n",0])
	lis4 = nex([lis2,"\n",0])
	print(lis3,lis4)

	sea = lis3


	com = []
	con = ["facebook","twitter","instagram"]
	bas = "https://www.google.com/search?q="
	for a,val in enumerate(sea):
		for b,val2 in enumerate(con):
			app = bas+val+" "+val2
			com.append(app)
	pri(com)
	num4([com,1])
	


inp = []
goo2(inp)