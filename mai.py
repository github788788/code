exec(open('util.py').read())
def mai(inp):
	atv = inp[0]
	pic = inp[1]
	ray = []
	ray.append(["u","usa2@email.com","Usausa1!"])
	ray.append(["s","sverige@europe.com","Svesve1!"])
	ray.append(["a","arlington@post.com","Arlarl1!"])
	ray.append(["v","violin78@mail.com","Viovio1!"])
	ray.append(["p","phone67@email.com","Phopho1!"])
	if pic=="":
		pic = geq(ray)
	cor = gcr(ray,pic)
	print (cor)
	usn = cor[1]
	pas = cor[2]
	atr = []
	if atv>0:
		hod3(["alt","tab",atv,atv])
	hod3(["ctrl","t",1,1])
	wri("https://www.mail.com/",2)
	but(["enter"],0,5)

	cf_ee("log in")
	hod3(["ctrl","f",1,1])
	but(["enter","enter","enter","esc"],0,1)
	hod3(["shift","tab",3,0])
	#wri(em,2)
	wri(usn[0:usn.find("@")],1)
	wri("@",1)
	wri(usn[usn.find("@")+1:len(usn)],1)
	but(["tab"],0,1)
	wri(pas,2)
	but(["enter"],0,4)
inp = []
mai(inp)