exec(open('util.py').read())
def fir(inp):
	
	dri = dri_([])
	acc = acc_([])

	#C:\Users\a\AppData
	fol = dri+"\\Users\\"+acc+"\\AppData"
	print(fol)

	#fol1 = fol+"\\"+

	ray = ["Local","LocalLow","Roaming"]

	for val in enumerate(ray):
		#print(val[1])
		val = val[1]
		spe = fol+"\\"+val+"\\Mozilla"
		print(spe)
		#os.remove(spe)

	#Local\\Mozilla
	#LocalLow\\Mozilla
	#Roaming\\Mozilla

inp = []
fir(inp)