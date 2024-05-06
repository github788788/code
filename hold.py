exec(open('util.py').read())
def hold(first,second,clicks,wait):
	pyautogui.keyDown(first)
	time.sleep(1)
	for a in range(0,clicks):
		pyautogui.press(second)
	pyautogui.keyUp(first)
	time.sleep(wait)
inp = []
hold(inp)