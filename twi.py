exec(open('util.py').read())
def twi(inp):
	
	alt(1,1)
	for a in range(0,20):
		"""
		#way 1
		hod3(["shift","tab",6,1])
		#key([["enter",1,0,1],["enter",1,0,1],["tab",2,0,1],["enter",1,0,1]])
		key([["enter",1,0,1],["enter",1,0,1],["enter",1,0,1]])	
		"""
		#way2
		pyautogui.click()
		time.sleep(1)	
		#pyautogui.click()
		key([["enter",2,0,0]])	


inp = []
twi(inp)