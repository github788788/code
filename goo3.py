exec(open('util.py').read())
def goo3(inp):
	
	#sea =str(input("search term = "))
	#sea = [sea]
	sea = whi2(["sea"])
	


	"""
	#print(tex)
	ide = "\n\n"
	dou = tex.find(ide)
	lis1 = tex[0:dou]
	lis2 = tex[dou:len(tex)]
	lis2 = lis2.replace(ide,"")
	print(lis1,lis2)
	lis3 = nex([lis1,"\n",0])
	lis4 = nex([lis2,"\n",0])
	print(lis3,lis4)
	"""
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
goo3(inp)