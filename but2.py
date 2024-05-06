exec(open('util.py').read())
def but2(ray):
	for a in range(0,len(ray)):
		for b in range(0,ray[a][0]):
			pyautogui.press(ray[a][1])


inp = []
but2(inp)