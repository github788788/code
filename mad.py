exec(open('util.py').read())
def mad(inp):
	inp = inp
	"""
	pyautogui.moveTo(pox, 725)	
	pyautogui.mouseDown()
	pyautogui.moveTo(pox, 360)
	pyautogui.mouseUp()
	"""
	num =int(input("how many = "))
	
	loc = pyautogui.position()
	print (loc)
	#sye()
	for a in range(0,num):
		pyautogui.click(x=252, y=148)
		time.sleep(1)
		pyautogui.click(x=229, y=185)
		time.sleep(1)
		pyautogui.click(x=284, y=141)
		time.sleep(1)

inp = []
mad(inp)