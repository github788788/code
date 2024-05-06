exec(open('util.py').read())
def bac(inp):
	
	ema = []
	ema.append("media788788@gmail.com")
	ema.append("desk788788@gmail.com")
	ema.append("violin78@protonmail.com")
	ema.append("cello34@protonmail.com")
	ema.append("violin78@mail.com")
	ema.append("usa2@email.com")

	ema2 = ""
	for a,val in enumerate(ema):
		ema2 = ema2+str(val)+","


	"""
	sub =str(input("subject = "))
	inf = str(input("info = "))	
	"""
	tex = rea4(["bac","txt"])
	tex = tex.replace("--- double new line is splitter between sub and bod, sub is first line, then after double new line is bod ---\n","")
	print(tex)
	ide = "\n\n"
	ide2 = tex.find(ide)
	sub = tex[0:ide2]
	inf = tex[ide2:len(tex)]
	inf = inf.replace(ide,"")
	print ("sub",sub)
	print ("bod",inf)


	att = str(input("attachments, blank if nothing = "))
	
	alt(1,1)
	cf_este3(["compose",0,0])

	tex = [ema2]
	tex.append(sub)
	tex.append(inf)
	
	cop([tex,0])
	key([["tab",1,0,1]])
	cop([tex,1])
	key([["tab",1,0,1]])
	cop([tex,1])

	fol = "E:\\Users\\-\\Downloads"
	fol2 = fol+"\\"
	fil = fol2+att
	
	key([["tab",1,0,1]])
	if len(att)>0:
		key([["tab",2,0,1]])
		key([["enter",1,0,1]])
		wri(fil,1)
		key([["down",1,0,1]])
		key([["enter",1,0,1]])
		time.sleep(2)
		cf_este3(["send",0,0])
	else:
		key([["tab",1,0,1]])
		key([["enter",1,0,0]])


			
inp = []
bac(inp)