exec(open('util.py').read())
def res6(inp):
	yee = "yee"
	hod3(["alt","space",1,0])
	for a in range(0,4):
		but(["down"],0,0)
	but(["enter"],0,0)
	pyautogui.keyDown("win")
	for a in range(0,len(inp)):
		but([inp[a]],0,0)
	pyautogui.keyUp("win")
	time.sleep(1)
	but(["esc"],0,0)

inp = []
res6(inp)