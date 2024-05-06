exec(open('util.py').read())
def lt2(ray,out):
	te = ""
	for a in range(0,len(ray)):
		te = te+ray[a]+"\n"
	#na = os.path.basename(__file__)
	#na = na.replace(".py","")
	na = out
	f= open(na+".txt","w")
	f.write(te)
	f.close() 

inp = []
lt2(inp)