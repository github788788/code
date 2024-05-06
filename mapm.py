exec(open('util.py').read())
def mapm():
	con = rea4([["mapm2"],'txt'])
	ray = genl([con])
	print (ray)

	#sys.exit()
	url = "https://www.google.com/maps/place/"
	ray2 = []
	inp = []
	for a in range(0,len(ray)):
		val = ray[a]
		inp.append(ray[a])
		new=url+val
		ray2.append(new)
	print( "ray2",ray2)
	print (len(ray2))
	#sys.exit()
	nu(ray2,1)
	pgu(len(ray2),0)
	for a in range(0,len(ray2)):
		val = inp[a]
		time.sleep(1)
		cf_ee2(val,0,1)
		#time.sleep(2)
		cf_ete2("satell")
		#cf_et("satell")
		time.sleep(1)
		if a<len(ray2)-1:
			hod3(["ctrl","pagedown",1,0])
inp = []
mapm(inp)