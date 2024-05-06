exec(open('util.py').read())
def gcr(ray,pic):
	for a in range(0,len(ray)):
		if pic==ray[a][0]:
			bac = ray[a]
			break
	return bac
inp = []
gcr(inp)