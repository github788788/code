exec(open('util.py').read())
def fof2(inp):
	ray = inp
	cop = "cop"
	tex = ""
	qua = 0
	for a in range(0,len(ray)):
		val = ray[a][0]
		if val=="cop":
			print (ray[a][1])
			tex = tex+ray[a][1]+"\n"
			qua = qua+1
	new = open("fof.txt","w")
	new.write(tex)
	new.close() 
	mat = 0
	num = 0
	for a in range(0,len(ray)):					
		val = ray[a]
		if len(val)==1:
			val()
			"""
			typ = type(val)
			if "func" in typ:
			#if type(val)==function
				val()
			#if "str" in typ:
			"""
		if len(val)==2:
			val = ray[a][0]
			if val!="cop":
				ray[a][0](ray[a][1])




			if val=="cop":
				hod3(["ctrl","a",1,0])
				hod3(["ctrl","v",1,1])	
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
fof2(inp)