exec(open('util.py').read())
def hd(first,second,clicks,wait):
	pyautogui.keyDown(first)
	for a in range(0,clicks):
		pyautogui.press(second)
	pyautogui.keyUp(first)
	time.sleep(wait) 
inp = []
hd(inp)