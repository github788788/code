exec(open('util.py').read())
def gev(tef,ide,stl):
	txt = rt(tef)
	cou = txt.count(ide)
	beg = 0
	ray = []
	for a in range(0,cou):
		sta = txt.find(ide,beg)
		nev = txt[sta:sta+stl]
		ray.append(nev)
		beg = sta+1
	return ray
inp = []
gev(inp)