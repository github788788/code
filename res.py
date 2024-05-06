exec(open('util.py').read())
def res(inp):
	com = inp[0]
	dow = inp[1]

	ray = []
	ray.append(["r",["right"]])
	ray.append(["l",["left"]])
	ray.append(["rd",["right","right","down"]])
	ray.append(["ld",["left","left","down"]])
	ray.append(["ru",["right","right","up"]])
	ray.append(["lu",["left","left","up"]])

	spe = ""
	for a,val in enumerate(ray):
		if com==val[0]:
			spe = val[1]
			break

	hod3(["alt","space",1,0])
	for a in range(0,dow):
		but3([["down"],0,0])
	but3([["enter"],0,1])
	pyautogui.keyDown("win")
	for a,val in enumerate(spe):
	#for a in range(0,len(loc)):
		#but(val,0,0)
		but3([[val],0,0])
	pyautogui.keyUp("win")
	time.sleep(1)
	but3([["esc"],0,0])


	"""
	for a in range(0,len(ray)):
		val = ray[a][0]
		if com==val:
			loc = ray[a][1]
			#at(1,1)

			#def res6(inp):
			yee = "yee"
			hod3(["alt","space",1,0])
			for a in range(0,dow):
				but(["down"],0,0)
			but(["enter"],0,0)
			pyautogui.keyDown("win")
			for a in range(0,len(loc)):
				but([loc],0,0)
			pyautogui.keyUp("win")
			time.sleep(1)
			but(["esc"],0,0)


			#res6(loc)
			#break
			"""inp = []
res(inp)