exec(open('util.py').read())
def rtr(ra,sp):
	r2 = []
	for a in range(0,len(ra)):
		nr = []
		th = ra[a]
		th = th+sp
		if th[0]=="\n":
			th = th[1:len(th)]
		co = th.count(sp)
		st = 0
		for b in range(0,co):
			en = th.find(sp,st)
			li = th[st:en]
			nr.append(li)
			st = en+1
		r2.append(nr)
	return r2
inp = []
rtr(inp)