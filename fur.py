exec(open('util.py').read())
def fur(pic,ind1,ray,ind2,ind3):
	for a in range(0,len(ray)):
		if pic==ray[a][ind1]:
			ray[a][ind2](ray[a][ind3])
			break
inp = []
fur(inp)