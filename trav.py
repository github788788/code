exec(open('util.py').read())
def tra(ray):

	url = []
	url.append("https://www.bahn.com/en")
	url.append("https://www.directferries.com/")
	url.append("snalltaget.se")	
	nu(url,1)
	pgu(len(ray),1)
	cf_etm("booking",2)	
	wri("berlin",5)
	but(["down","down","tab"],0,0)
	wri("rostock",5)
	but(["down","tab","tab"],0,0)
	wri("08:00",5)
	but(["enter"],0,0)
	hod3(["ctrl","pagedown",1,1])
	cf_etm("special o",1)
	but(["right","tab"],0,0)
	wri("Rostock - Trelleborg",5)
	but(["down","enter"],0,0)


	"Rostock - Trelleborg"
inp = []
tra(inp)