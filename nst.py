exec(open('util.py').read())
def nst(ray):
	url = ray[0]
	loc = ray[1]
	wai = ray[2]
	htb("ctrl","shift","p",1,1)
	res4(loc,1)
	wri(url,wai)
	but(["enter"],0,0)
	"""
inp = []
nst(inp)