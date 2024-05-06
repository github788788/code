exec(open('util.py').read())
def dow(ray):
	ray = ray
	#fil = whi("keywords in files = ")
	sou = []
	sou.append("1 for from file, 2 for input")
	sou = fol2(sou)
	sou = int(sou[0][1])
	if sou==1:
		fil = ger([rt("dow"),"\n"])
	if sou==2:
		fil = fil = whi("keywords in files = ")
		
	print(fil)
	#sys.exit()	

	fol = "A:\\Users\\-\\Downloads"
	
	lis = os.listdir(fol)

	#print (lis)
	for a,val in enumerate(lis):
		val = val.lower()
		for b, val2 in enumerate(fil):
			if val2 in val:
				print (val)
				src = "A:\\Users\\-\\Downloads"+"\\"+val
				dst = "C:\\Users\\Administrator\\Downloads"+"\\fro\\"+val
				shutil.copy(src,dst)
				os.remove(src)


	print (fil)


inp = []
dow(inp)