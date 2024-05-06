exec(open('util.py').read())
def ant():
	#url = "https://mss.anthem.com/va/login.html#/login"
	url = "https://mss.anthem.com/va/login.html"
	usn = "violin78"
	pas = "Vivivi1!"
	inp = []
	inp.append([neu3,[url,2,5]])
	inp.append([cf_et3,["user n",1,0]])
	inp.append([usn])
	inp.append([but3,[["tab"],0,0]])
	inp.append([pas])
	inp.append([but3,[["enter"],0,5]])
	inp.append([cf_etst,["mikael"]])
	inp.append([but3,[["tab","tab","tab","enter"],0,0]])
	fof3(inp)
	
inp = []
ant(inp)