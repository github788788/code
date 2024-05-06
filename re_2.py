exec(open('util.py').read())
def re(wa,ra,es):
	time.sleep(wa)
	pyautogui.keyDown("win")
	for a in range(0,len(ra)):
		but([ra[a]],0,0)
	pyautogui.keyUp("win")
	if es==1:
		time.sleep(1)
		pyautogui.press("esc")
		time.sleep(1)
		#inp = []
re(inp)