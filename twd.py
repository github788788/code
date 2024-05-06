exec(open('util.py').read())
def twd(inp):
	first_hold = inp[0]
	second_hold = inp[1]
	button_click = inp[2]
	clicks = inp[3]
	wait = inp[4]

	pyautogui.keyDown(first_hold)
	pyautogui.keyDown(second_hold)
	time.sleep(1)
	for a in range(0,clicks):
		pyautogui.press(button_click)
	pyautogui.keyUp(first_hold)
	pyautogui.keyUp(second_hold)
	time.sleep(wait)
inp = []
twd(inp)