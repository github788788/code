exec(open('util.py').read())
def fol2(ray):
	inp = []
	for a,val in enumerate(ray):
		bac =str(input(val+" = "))
		#bac =str(input(val))
		inp.append([val,bac])
	return inp	


inp = []
fol2(inp)