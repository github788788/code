exec(open('util.py').read())
def caf(inp):
		#pos = pyautogui.position()
		#print (pos,type(pos))
		mon =str(input("start mon = "))
		day =str(input("start day = "))
		how =int(input("add how many  = "))
		alt(1,1)
		tex2 = mon+"."+day
		tex = []
		for a in range(0,how):
			new = mon+"."+str(int(day)+a)
			tex.append(new)	
		pos = pyautogui.position()
		pyautogui.click()
		print(pos,pos[0],pos[1])
		xco=pos[0]
		yco=pos[1]

		for a,val in enumerate(tex):
			#pyautogui.moveTo(300, 700)	
			pyautogui.moveTo(xco, yco)	
			hod3(["shift","f11",1,2])
			pyautogui.rightClick()
			#pyautogui.moveTo(300, 500)	
			pyautogui.moveTo(xco, yco-200)	
			pyautogui.click()
			wri(val,1)
			key([["enter",1,0,2]])
		hod3(["alt","down",1,2])

		pos = pyautogui.position()
		pyautogui.moveTo(60, 190)
		pyautogui.click()
		pyautogui.keyDown("shift")	
		pyautogui.moveTo(220, 190)
		pyautogui.click()
		hod3(["ctrl","c",1,1])

		for a,val in enumerate(tex):
			hod3(["alt","up",1,2])
			pyautogui.moveTo(60, 190)
			pyautogui.click()
			hod3(["ctrl","c",1,1])


inp = []
caf(inp)