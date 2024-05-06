exec(open('util.py').read())
def gre(ray):
	inp = []
	inp.append("from")
	inp.append("to")
	inp.append("month")
	inp.append("day")
	
	inp = fol(inp)
	print (inp)
	
	dep = inp[0]
	arr = inp[1]	
	mon = inp[2]	
	day = inp[3]
	ext = [mon,day]
	

	def adz(inp):
		bac = []
		for a,val in enumerate(inp):
			val = str(val)
			if len(val)==1:
				inp[a] = "0"+str(val)
				bac.append(val)
			#bac.append(new)
		return inp

	ext = adz(ext)
	mon = ext[0]
	day = ext[1]


	print (mon,day)
	#sys.exit()


	dat = mon+"/"+day+"/2021"	


	url = "greyhound.com"
	urr = []
	urr.append(url)
	num4([urr,1])
	cf_etm3(["from",1])
	wri(dep,1)
	but3([["tab","tab","tab"],0,0])
	wri(arr,1)
	but3([["tab","tab"],0,0])
	wri(dat,1)
	cf_este3(["search",0,0])
inp = []
gre(inp)