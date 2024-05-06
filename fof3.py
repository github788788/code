exec(open('util.py').read())
def fof3(inp):
	ray = inp
	cop = "cop"
	tex = ""
	qua = 0
	ini = 0
	neu = ""
	for a in range(0,len(ray)):
		val = ray[a]
		if len(val)==1:
			val2 = val[0]
			typ = str(type(val2))
			if "str" in typ:
				tex = tex+ray[a][0]+"\n"
				qua = qua+1
		if len(val)==2:
			#val2 = val[0]
			if ini==0:
				if init in val:
					ini = 1
			if neu=="":
				if neu3 in val:
					neu = a
	if ini==0:
		if neu=="":
			ray.insert(0,[init,["fof.txt"]])
		if neu!="":
			ray.insert(neu+1,[init,["fof.txt"]])
	print (ini,neu)
	print (tex)
	#sys.exit()
	new = open("fof.txt","w")
	new.write(tex)
	new.close() 
	mat = 0
	num = 0
	for a in range(0,len(ray)):					
		val = ray[a]
		if len(val)==2:
			ray[a][0](ray[a][1])
		if len(val)==1:
			val = val[0]
			typ = str(type(val))
			if "func" in typ:
				val()
			if "str" in typ:
				hod3(["ctrl","a",1,0])
				hod3(["ctrl","v",1,0])	
				num = num+1	
				if num==qua:
					continue
				if num<=qua-1:
					at(1,1)
					hod3(["shift","down",1,0])
					hod3(["ctrl","c",1,0])
					but(["right"],0,0)
					if num==qua-1:
						af4(1,1)
					if num<qua-1:
						at(1,1)
inp = []
fof3(inp)