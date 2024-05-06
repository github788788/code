exec(open('util.py').read())
def resc(com):

	ray = []
	ray.append(["r",["right"]])
	ray.append(["l",["left"]])
	ray.append(["rd",["right","right","down"]])
	ray.append(["ld",["left","left","down"]])
	ray.append(["ru",["right","right","up"]])
	ray.append(["lu",["left","left","up"]])


	for a in range(0,len(ray)):
		val = ray[a][0]
		if com==val:
			loc = ray[a][1]
			#at(1,1)
			#res6(loc)
			hod3(["alt","space",1,0])
			for a in range(0,5):
				but(["down"],0,0)
			but(["enter"],0,0)
			pyautogui.keyDown("win")
			#for a in range(0,len(inp)):
			#	but([inp[a]],0,0)
			for a in range(0,len(loc)):
				but([loc[a]],0,0)
			pyautogui.keyUp("win")
			time.sleep(1)
			but(["esc"],0,0)


			break

			"""inp = []
resc(inp)