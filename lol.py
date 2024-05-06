exec(open('util.py').read())
def lol(fil):
	con = rt(fil)
	cou = con.count("\n")
	lis = []
	beg = 0
	for a in range(0,cou+1):
		fin = con.find("\n",beg)
		if fin<0:
			fin=len(con)
		spe = con[beg:fin]
		if len(spe)>0:
			lis.append(spe)
		beg = fin+1
	return lis
inp = []
lol(inp)