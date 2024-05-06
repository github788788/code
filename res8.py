exec(open('util.py').read())
def res8(com):

	def res88(com):

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
				res6(loc)
				break

	#inp = []
	#inp.append("location")
	#inp = ask(inp)
	#loc = inp[0][1]
	res88(com)







	
	
	"""
	if es==1:
		time.sleep(1)
		pyautogui.press("esc")
		time.sleep(1)
	"""
inp = []
res8(inp)