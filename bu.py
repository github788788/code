exec(open('util.py').read())
def bu():
	bm = str(input("flixbus month = "))
	bd = str(input("flixbus day = "))
	br = []
	br.append(bd)
	br.append(bm)
	for a in range(0,len(br)):
		if len(br[a])==1:
			br[a] = "0"+br[a]
	bt = br[0]+"."+br[1]+"."+"2020"
	print(bt)
	bu = "https://shop.flixbus.se/search?departureCity=6678&arrivalCity=3798&route=Helsingborg-Stockholm&rideDate="
	bu = bu+bt
	bu = bu+"&adult=1&_locale=sv&features%5Bfeature.darken_page%5D=1&wt_eid=2159782325479787168&wt_t=1597823291545&affiliate=%28not+set%29%2C"
	#urls.append(bu)
	hod3(["alt","tab",1,0])
	hod3(["ctrl","t",1,0])
	wri(bu,2)
	but(["enter"],0,0)
inp = []
bu(inp)