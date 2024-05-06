exec(open('util.py').read())
def r2(ra):
	pyautogui.keyDown("win")
	for a in range(0,len(ra)):
		b2([ra[a]],0,0)
	pyautogui.keyUp("win")
	time.sleep(1)
	b2(["esc"],0,1)
	
inp = []
r2(inp)