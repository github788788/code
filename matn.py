exec(open('util.py').read())
def matn(inp):
	spe = inp[0]
	ray = inp[1]
	ide = inp[2]
	bac = inp[3]
	ret = spe
	for a,val in enumerate(ray):
		print (val[ide])
		if val[ide]==spe:
			ret = val[bac]
			#return val[bac]
			break
	return ret




inp = []
matn(inp)