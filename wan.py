exec(open('util.py').read())
def wan():
	ray = []
	ray.append(["From"])
	ray.append(["To"])
	ray.append(["Month"])
	ray.append(["Day"])
	dev = 1
	if dev==0:
		for a in range(0,len(ray)):
			ray[a].append((input(ray[a][0]+" = ")))
	if dev==1:

		"""
		app = ["charlottesville, va","washington dc","10","25"]
		for a in range(0,len(app)):
			ray[a].append(app[a])
			"""
		ray = inr2(ray)

	url = "https://www.wanderu.com/en-us/depart/"
	ura = []
	for a in range(0,2):
		ura.append(ray[a][1]+"/")
	ura.append("2020")
	for a in range(2,len(ray)):
		ura.append("-"+ray[a][1])
	for a in range(0,len(ura)):
		url = url+ura[a]

	print(url)
	#sys.exit()
	#neu(url,2,7)
	url = [url]
	num4([url,1])

	cf_este2("cheape",0)
inp = []
wan(inp)