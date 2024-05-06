exec(open('util.py').read())
def bla(ray):
		for a in range(0,len(ray)):
			val = ray[a][1]
			val = str(val)
			if len(val)==0:
				val=0
			ray[a][1]=val
		return ray


			inp = []
bla(inp)