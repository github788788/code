exec(open('util.py').read())
def ren(inp):
	def rep2(inp):
		#val2 = rep2([val,rep])
		#inp[0] = str/array to be worked on
		#inp[1] = replist
		two = inp[0]
		trep = inp[1]
		for a,val in enumerate(trep)
			old = val[0]
			new = val[1]
			two = two.replace(old,new)
		return two

	cwd = os.getcwd()
	#fol =cwd+"\\ear" 
	fol = cwd
	lis = os.listdir(fol)

	old = "exec(open('bas2.py').read())"
	new = "exec(open('util.py').read())"
	trep = []
	trep.append([old,new])

	for a,val in enumerate(lis):
		if ".py" in val:
			try:
				tex = rea([val])
			except:
				continue
			val2 = rep2([val,trep])
			wri2([val,tex2])
			#os.rename(old,new)
			#os.remove(fil)

inp = []
ren(inp)