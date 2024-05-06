exec(open('util.py').read())
def rer(inp):
	fol = os.getcwd()
	fol = fol.replace("0c","Downloads")
	lis = os.listdir(fol)
	for a,val in enumerate(lis):
		val = val[0:len(val)-4]
		if len(val)<=3:
			continue
		hit = 0
		for b,val2 in enumerate(lis):
			ori = []
			ori.append(val2)
			ori = ori[0]

			val2 = val2[0:len(val2)-4]

			if val in val2:
				if val!=val2:
					hit = hit+1
			if hit>0:
				print ("val1",val)
				print ("val2",val2)
				hit = 0
				os.remove(fol+"\\"+ori)
	
inp = []
rer(inp)