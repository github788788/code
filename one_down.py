exec(open('util.py').read())
def one_down(first,second,wait):
	pyautogui.keyDown(first)
	pyautogui.press(second)
	pyautogui.keyUp(first)
	time.sleep(wait) inp = []
one_down(inp)