exec(open('util.py').read())
def gel(tef,ide):
	#txt = rt(tef)
	txt = tef
	cou = txt.count(ide)
	beg = 0
	ray = []
	for a in range(0,cou+1):
		if a==0:
			sta = 0
			end = txt.find(ide)
		if a>0:
			sta = txt.find(ide,beg)
			end = txt.find(ide,sta+len(ide))
		if end<0:
			end = len(txt)
		nev = txt[sta:end].replace("\n","")
		ray.append(nev)
		beg = sta+1
	return ray

inp = []
gel(inp)