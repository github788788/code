exec(open('util.py').read())
def mwh2(inp):
	url = "https://mychart.mwhc.com/mychart/Billing/Details?ID=WP-24BZ0G8iQup-2B0YpR6dV6umeQ-3D-3D-24HyCPRBVi9Tsd0DWVi57-2Bv0ZSpX9HMaYHmhQB7Yh07WI-3D&Context=WP-24kaa7uki37RKmJYXx9C3DdQ-3D-3D-24w-2B8Fh5dBnlLOcSy9SzR8Eu1gObDNVjvEi30vpI14S7s-3D"	
	usn = "mwhos"
	pas = "mwhos123"
	ray = []
	"""
	ray.append([hod3,["alt","tab",1,1]])	
	ray.append([hod3,["alt","tab",2,1]])	
	"""
	ray.append([hod3,["ctrl","t",1,1]])	
	ray.append([url])
	ray.append([but3,[["enter"],0,3]])
	#ray.append([neu3,[url,3,5]])
	#ray.append([cf_et5,["account",1,1]])	
	ray.append([usn])
	ray.append([but3,[["enter"],0,3]])
	"""
	ray.append([usn])
	ray.append([but3,[["enter"],0,3]])
	"""
	ray.append([pas])
	ray.append([but3,[["enter"],0,0]])
	#fof3(inp)
	raf(ray)


inp = []
mwh2(inp)