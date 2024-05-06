exec(open('util.py').read())
def sta2(inp):
	inp = inp

	#al4 = str(input("1 to alt f4 first firefox, otherwise click to continue = "))
	al4 = str(input("1 if firefox already up, otherwise click to continue = "))
	net = str(input("network, 1 for coordinate, otherwise click to continue = "))

	if al4=="1":
		at(1,1)
		#af4(1,1)

	if al4!="1":
		sw("C:\Program Files\Mozilla Firefox\\firefox.exe",0)	
		inp =str(input("click if firefox has loaded = "))
		at(1,1)



	if net=="1":
		but(["win"],0,2)
		wri("network",1)
		but(["enter"],0,3)
		wri("connect network",1)
		but(["enter"],0,2)
		num = 9
		for a in range(0,num):
			but(["tab"],0,0)
		but(["enter"],0,0)

		con = str(input("click to continue = "))
		at(1,1)
		
	#sys.exit()
	
	def nst(ray):
		url = [ray[0]]
		loc = ray[1]
		wai = ray[2]
		htb2("ctrl","shift","p",1,1)
		time.sleep(1)
		#res4(loc,1)
		#res5(loc)
		res7(loc)
		nu(url,0)
		#wri(url,wai)
		#but(["enter"],0,0)

	#at(1,1)
	mor = []
	
	new = []
	#new.append("https://www.google.com/maps/place/Ficklin+Bryant+Upholstery/@37.9498038,-76.6520033,3a,37.5y,313.4h,84.47t/data=!3m6!1e1!3m4!1sPui3MfF8zdBh8dwNMnoAvw!2e0!7i13312!8i6656!4m5!3m4!1s0x89b74d927effafb3:0x9c5e6124c37926cf!8m2!3d37.94981!4d-76.653013")
	new.append("C:\\Users\\-\\Documents\\Lightshot\\hay7.jpg")
	#new.append(["right"])
	new.append("ru")

	new.append(2)
	mor.append(new)

	new = []
	#new.append("https://www.google.com/maps/place/Haynesville,+VA+22572,+USA/@37.950222,-76.6624244,3a,75y,255.53h,63.82t/data=!3m7!1e1!3m5!1sawcwhA8Vl_KMcqzBg7OTcQ!2e0!6s%2F%2Fgeo0.ggpht.com%2Fmaps%2Fphotothumb%2Ffd%2Fv1%3Fbpb%3DChEKD3NlYXJjaC5nd3MtcHJvZBIgChIJCbTeu5VNt4kRX8QHR7p2KiUqCg0AAAAAFQAAAAAaBAhWEFY%26gl%3DSE!7i13312!8i6656!4m5!3m4!1s0x89b74d95bbdeb409:0x252a76ba4707c45f!8m2!3d37.9501331!4d-76.6624565")
	new.append("C:\\Users\\-\\Documents\\Lightshot\\fbu2.jpg")
	#new.append(["left"])
	new.append("lu")
	new.append(2)
	mor.append(new)
	
	
	new = []
	#new.append("youtube.com")
	new.append("")
	
	#new.append(["left","left","down"])
	new.append("ld")
	
	new.append(1)
	mor.append(new)
	
	"""
	for a in range(0,len(mor)):
		nst(mor[a])
		if a==0:
			at(1,1)
			af4(1,1)
	exec(open('ham.py').read())
	"""
	htb("ctrl","shift","p",1,1)

	hod3(["alt","tab",1,1])
	hod3(["alt","f4",1,1])
		

	#res5(["right","right","down"])
	res5(["right"])
	at(1,1)
	exec(open('owl.py').read())	

	htb("ctrl","shift","p",1,1)
	res5(["left"])

	
	#you = "https://www.youtube.com/watch?v=ynZApvZXEqg&list=RDCMUC_EVGyh8dABzKl0LwTw45mw&start_radio=1"

	you = "https://www.youtube.com/watch?v=kOsVL5_AKow&t=28s"
	#url = ["youtube.com"]
	url = []
	url.append(you)
	#url.append("maps.google.com")
	url.append("https://www.google.com/maps/place/Stockholm,+Sweden/@59.3258429,17.7025686,10z/data=!3m1!4b1!4m5!3m4!1s0x465f763119640bcb:0xa80d27d3679d7766!8m2!3d59.3293235!4d18.0685808")
	nu(url,0)

	exec(open('sky.py').read())

	#exec(open('gma.py').read())	

inp = []
sta2(inp)