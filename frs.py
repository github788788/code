exec(open('util.py').read())
def frs(inp):
	tex = inp[0]
	ide = inp[1]
	qui = 0
	bac = []
	sta = 0
	while(qui<1):
		end = tex.find(ide,sta)
		if end<0:
			end =len(tex)
			qui=1
		lin = tex[sta:end]
		bac.append(lin)
		sta = end+len(ide)

	return bac


inp = []
frs(inp)