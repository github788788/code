exec(open('util.py').read())
def ant2(inp):


	url = "https://mss.anthem.com/va/secure/claims.html#/claims"
	usn = "violin78"
	pas = "Vivivi1!"
	ray = []
	"""
	ray.append([hod3,["alt","tab",1,1]])	
	ray.append([hod3,["alt","tab",2,1]])	
	"""
	ray.append([hod3,["ctrl","t",1,1]])	
	ray.append([url])
	ray.append([but3,[["enter"],0,3]])

	ray.append([cf_et3,["user n",1,0]])
	ray.append([usn])
	
	#ray.append([neu3,[url,3,5]])
	#ray.append([cf_et5,["account",1,1]])	
	#ray.append([usn])
	ray.append([but3,[["tab"],0,1]])
	"""
	ray.append([usn])
	ray.append([but3,[["enter"],0,3]])
	"""
	ray.append([pas])
	ray.append([but3,[["enter"],0,0]])
	#fof3(inp)
	raf(ray)

inp = []
ant2(inp)