exec(open('util.py').read())
def upd(inp):
	num = inp[0]
	#num = num
	#num = 2
	fol = os. getcwd()
	if num=="dri":
		fol3 = fol[0:fol.find(":")+2]
	if num!="dri":
		fol2 = fol[::-1]
		beg = 0
		fin = 0

		for a in range(0,num):
			fin = fol2.find("\\",beg)
			beg = fin+1
		fol3 = fol[0:len(fol)-fin]
	return fol3
	#fol = upd([1])
inp = []
upd(inp)