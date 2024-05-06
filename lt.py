exec(open('util.py').read())
def lt(ra):
	te = ""
	for a in range(0,len(ra)):
		te = te+ra[a]+"\n"
	na = os.path.basename(__file__)
	na = na.replace(".py","")
	f= open(na+".txt","w")
	f.write(te)
	f.close() 
	"""inp = []
lt(inp)