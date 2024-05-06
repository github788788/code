exec(open('util.py').read())
def cha(inp):
	
	cwd = os.getcwd()
	fol =cwd+"\\ear" 
	lis = os.listdir(fol)

	for a,val in enumerate(lis):
		if ".pri" in val:
			fil = fol+"\\"+val
			print(a,fil)
			#pri(fil)
			loa = rec(["mas"])
			pri(loa)



inp = []
cha(inp)