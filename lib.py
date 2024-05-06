exec(open('util.py').read())
def lib(inp):

	roo1 =str(input("was in room number = "))
	roo2 =str(input("move to room number = "))
	
	hou =str(input("hour = "))
	miu =str(input("minute = "))

	hou2 = str(int(hou)+2)

	tim1 = hou+":"+miu
	tim2 = hou2+":"+miu
	tex = "Hi, I was in room "+roo1+" at the Fredericksburg library, I was curious, was room "+roo2+" available from "+tim1+" to "+tim2+"?"

	url = "https://www.librarypoint.org/ask/"

	num4([[url],2])

	cf_et("which location")
	key([["f",1,0,1],["tab",1,0,1]])
	wri(tex,3)

	#which location
	
	

	#https://www.librarypoint.org/ask/

	print(tex)

inp = []
lib(inp)