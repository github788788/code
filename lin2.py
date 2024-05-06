exec(open('util.py').read())
def lin2(fil):
	tex = rt(fil)
	cou = tex.count("\n")
	lis = []
	beg = 0
	for a in range(0,cou+1):
		fin = tex.find("\n",beg)
		if fin<0:
			fin = len(tex)
		spe = tex[beg:fin]
		lis.append(spe)
		beg = fin+1
	return lis

	inp = []
lin2(inp)