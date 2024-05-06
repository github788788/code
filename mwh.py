exec(open('util.py').read())
def mwh():

	usn = "mwhos"
	pas = "mwhos123"
	inp = []
	inp.append([neu3,["https://mychart.mwhc.com/mychart/Authentication/Login?",2,5]])
	#inp.append([init,["fof.txt"]])
	inp.append([usn])
	#inp.append([cf2,["logga in",1]])
	inp.append([but3,[["tab"],0,0]])
	inp.append([pas])
	inp.append([but3,[["enter"],0,5]])

	inp.append([cf_etste3,["menu"]])
	inp.append([cf_ete3,["billing"]])
	inp.append([cf_ee3,["view a"]])
	inp.append([cf_ee3,["details"]])

	cf_ete3
	

	#inp.append([cf_este3,["logga in",1,1]])
	"""
	inp.append([pas])
	inp.append([but3,[["enter"],0,0]])
	"""
	"""
	url = "https://mychart.mwhc.com/mychart/Billing/Details?ID=lcNVZlfzZdiZRZIB0pWBLQ%3d%3d&Context=sp66lxgw1xQ4K3vSbRGWlA%3d%3d"
	inp.append([neu3,[url,3,5]])
	inp.append([cf_ee3,["detail"]])
	"""

	fof3(inp)




inp = []
mwh(inp)