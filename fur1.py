exec(open('util.py').read())
def fur1(ray,ver):
	for a in range(0,len(ray)):
		if ver==ray[a][0]:
			ray[a][1]()
			breakinp = []
fur1(inp)