exec(open('util.py').read())
def fol(ray):
	inp = []
	for a,val in enumerate(ray):
		bac =str(input(val+" = "))
		inp.append(bac)
	return inp	
inp = []
fol(inp)