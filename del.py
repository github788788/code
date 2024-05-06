exec(open('util.py').read())
def dee():
	import pyautogui,time
	def but(ray,between_wait,end_wait):
		for a in range(0,len(ray)):
			pyautogui.press(ray[a])
			time.sleep(between_wait)
		time.sleep(end_wait)
	to_end = int((input("to end, 0 for no, 1 for yes? = ")))
	how_many = (input("how many? = "))
	how_many = int(how_many)
	hod3(["alt","tab",1,1])
	if to_end==1:
		hod3(["ctrl","9",1,1])
	pyautogui.keyDown("ctrl")
	for a in range(0,how_many):
		but(["f4"],0,0)
	pyautogui.keyUp("ctrl")
dee()