exec(open('util.py').read())
def res4(ra,esc):
	#time.sleep(wa)
	pyautogui.keyDown("win")
	for a in range(0,len(ra)):
		but([ra[a]],0,0)
	pyautogui.keyUp("win")
	if esc==1:
		time.sleep(1)
		but(["esc"],0,1)

inp = []
res4(inp)