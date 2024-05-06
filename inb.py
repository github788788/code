exec(open('util.py').read())
def inb(ray):
	ray = ray

	inp = []
	#inp.append("time delete")
	#inp.append("time trash")

	inp.append("delete(d),trash(t),both(b), or spam(s)")
	inp.append("loops")
	inp = fol(inp)

	com = inp[0]
	num = int(inp[1])



	print (inp)
	#sys.exit()
	alt(1,1)
	
	def fri():
		cf_ee33(["inbox",2])
		cf("newest",1)
		but3([["esc"],0,0])
		hod3(["shift","tab",2,0])
		but3([["enter"],0,1])
		but3([["up","up","enter"],0,1])
		hod3(["shift","tab",2,0])
		but3([["space","t"],1,0])
		#cf_ee33(["trash",2newest])
	

	#cf_ete3(["spam"])
	def tra():
		#cf_ete33(["spam",1])
		cf("4.0.",1)
		key([["esc",1,0,0],["tab",2,0,0],["space",2,0,0]])
		cf("newest",1)
		but3([["esc"],0,0])
		#hod3(["shift","tab",5,1])
		hod3(["shift","tab",4,1])
		but3([["space"],0,0])
		
		hod3(["ctrl","backspace",3,1])
		but3([["tab","tab","enter"],0,1])

	def bot():
		fri()
		tra()
		#cf_ee3(["inbox"])

	def spa():
		cf_ee33(["spam",2])
		cf("newest",1)
		but3([["esc"],0,0])
		hod3(["shift","tab",2,0])
		but3([["enter"],0,1])
		but3([["up","up","enter"],0,1])
		hod3(["shift","tab",2,0])
		but3([["space","t"],1,0])
		#cf_ee33(["trash",2newest])
	

	ray = []
	ray.append(["d",[fri]])
	ray.append(["t",[tra]])
	ray.append(["s",[spa]])
	ray.append(["b",[bot]])

	for a in range(0,num):
		for b,val in enumerate(ray):
			if com==val[0]:
				val[1][0]()
				break
inp = []
inb(inp)