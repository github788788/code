exec(open('util.py').read())
def ran(inp):
	
	fil = "fil.txt"
	tex = rea([fil])
	#print(tex)
	tex2 = tex.replace(" ","\t")
	#print(tex2)
	#ray = []
	ray = nex3([tex2,"#","\n"])
	#pri(ray)
	for a,val in enumerate(ray):
		fir= val.find("\t")
		sec = val.find("\t",fir+1)
		thi = val.find("\t",sec+1)
		spe = val[thi:len(val)]
		#spe = val[fir:val.find("\t",fir+1)]
		spe = spe.replace("\t","")
		print(spe)
		#print("#"+val[0:val.find("\t")])

inp = []
ran(inp)