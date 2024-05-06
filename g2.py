exec(open('util.py').read())
def g2():
	bm = str(input("month = "))
	bd = str(input("day = "))
	br = []
	br.append(bd)
	br.append(bm)
	for a in range(0,len(br)):
		if len(br[a])==1:
			br[a] = "0"+br[a]
		
	print(br)
	da = br[1]+"."+br[0]
	return da

inp = []
g2(inp)