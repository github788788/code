exec(open('util.py').read())
def lat(inp):
	from os.path import exists
	ray = []
	for a in range(0,26):
		let = chr(a+97)
		res = exists(let + ':')
		if res==True:
			app = [let,res]
			ray.append(app)
	#pri(ray)
	fin = []
	for val in enumerate(ray):
		let = val[1][0]
		fol = let+":/Users"
		try:
			lis = os.listdir(fol)
		except:
			continue
		ski = ["All Users","Default","Default User","desktop.ini","Public",]
		use = []
		for valb in lis:
			if valb in ski:
				continue
			print(valb)
			use.append(valb)
		use2 = use[0]
		fil = fol+"/"+use2+"/Downloads/util.7z"
		tim = os.path.getmtime(fil)
		from datetime import datetime
		tim2 = datetime.fromtimestamp(tim, tz = None)
		app = [tim,use2,fil,tim2]
		fin.append(app)
		fin.sort(reverse=True)
	#pri(fin)
	lis1 = []
	lis2 = []
	end = []
	res = []
	for val in enumerate(fin):
		val2 = val[1]
		fol = val2[2]
		#print(val2)
		#print(tim)
		fol2 = fol.replace("Downloads/util.7z","")+"util"
		lis = os.listdir(fol2)
		che = []
		for val2 in enumerate(lis):
			#print(val2)
			fil = fol2+"/"+val2[1]
			tim = os.path.getmtime(fil)
			che.append([tim,fil])
			#print(tim)
		che.sort(reverse=True)
		#pri(che)
		app = [fol2]+che[0]
		res.append(app)
	pri(res)
	fol1 = res[0][0]
	fol2 = res[1][0]
	if "c:/" not in fol1:
		shutil.copytree(fol1,fol2)
		print(fol1,fol2)
	#shutil.copytree("tes", "tes2")

inp = []
lat(inp)