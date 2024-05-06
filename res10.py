exec(open('util.py').read())
def res10(inp):
	com = inp[0]
	wai = inp[1]
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

			#hod3(["alt","space",1,wai])
			hod3(["alt","space",1,wai])
			for b in range(0,4):
				but(["down"],0,0)
			but(["enter"],0,0)
			pyautogui.keyDown("win")
			for b in range(0,len(loc)):
				but([loc[b]],0,0)
			pyautogui.keyUp("win")
			time.sleep(1)
			but(["esc"],0,0)

			
	
			
			#res6(loc)
			break

inp = []
res10(inp)