exec(open('util.py').read())
def two_down(first,second,wait):
	pyautogui.keyDown(first)
	pyautogui.press(second)
	pyautogui.press(second)
	pyautogui.keyUp(first)
	time.sleep(wait) inp = []
two_down(inp)