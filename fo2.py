exec(open('util.py').read())
def fo2(ray):
	inp = []
	for a,val in enumerate(ray):
		inq = val+" = "
		bac =str(input(inq))
		#bac =str(input(val))
		inp.append([inq,bac])
	return inp	

inp = []
fo2(inp)