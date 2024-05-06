exec(open('util.py').read())
def ren2():
	fol = os.getcwd()
	lis = os.listdir(fol)
	rep = []
	"""
	rep.append(["write(","wri("])
	rep.append(["button(","but("])
	rep.append(["hold_down(","hod3(["]])
	"""
	#rep.append([".wri(","write("])
	rep.append(["fiwrite(","write("])
	for a in range(0,len(lis)):
		val = lis[a]
		if "bas.py" in val:
			continue
		if ".py" in val:
			cha = 0
			con = rt3([val,""])
			for b in range(0,len(rep)):
				if rep[b][0] in con:
					con = con.replace(rep[b][0],rep[b][1])
					cha = cha+1
			if cha>0:
				
				f= open(val,"w")
				f.write(con)
				f.close() 
				
				print (val)
			inp = []
ren2(inp)