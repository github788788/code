exec(open('util.py').read())
def edi(inp):	
	alt(1,1)
	for a in range(0,20):
		key([["enter",1,0,0]])
		hod3(["ctrl","home",1,0])
		hod3(["ctrl","down",1,0])
		hod3(["alt","enter",1,0])
		key([["enter",1,0,0]])
	
	"""

	cwd = os.getcwd()
	fea =cwd+"\\ear" 
	lis = os.listdir(fea)
	#pri(lis)
	inc = 0
	ski = 0
	for a,val in enumerate(lis):
		if ".csv" in val:
			if val.replace(".csv",".xls") in lis:
				ski = ski+1
				print(ski)
				continue
			#sye()
			inc = inc+1
			fil = fea+"\\"+val
			loa = csr([fil])
			#pri(loa)
			sav = fea+"\\"+val.replace(".csv","")+".xls"
			print(inc,val)
			xls2([loa,sav])
			print(sav)
			"""
			


inp = []
edi(inp)