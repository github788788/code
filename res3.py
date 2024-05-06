exec(open('util.py').read())
def res3(ra):
	#time.sleep(wa)
	pyautogui.keyDown("win")
	for a in range(0,len(ra)):
		but([ra[a]],0,0)
	pyautogui.keyUp("win")
	inp = []
res3(inp)