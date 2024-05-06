exec(open('util.py').read())
def ger(inp):

	con = inp[1]
	ide = inp[0]
	qui = 0
	ray = []
	sta = 0
	while(qui<1):
		#beg = con.find(ide,sta)
		beg = sta
		end = con.find(ide,beg+1)
		print("end",end)
		
		#print (end)
		if end<0:
			end = len(con)
			qui = 1
		lin = con[beg:end]
		lin = lin.replace(ide,"")
		print ("lin",lin)
		if len(lin)>0:
			ray.append(lin)
		sta = end
	return ray
	print (ray,len(ray))


inp = []
ger(inp)