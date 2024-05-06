exec(open('util.py').read())
def key3(ray):
	#pop = []
	for a,val in enumerate(ray):
		but = val[0]
		num = val[1]
		wai1 = val[2]
		wai2 = val[3]
		for a in range(0,num):
			pyautogui.press(but)
			time.sleep(wai1)
		time.sleep(wai2)


		#try:
		but = []
		print ("val[1]",val[1])
		for b in range(0,val[1]):
			but.append(val[0])
		print (but)
		but3([[but],val[2],val[3]])


inp = []
key3(inp)