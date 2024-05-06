exec(open('util.py').read())
def res2(ray1,ray2):
	#time.sleep(wa)
	pyautogui.keyDown("win")
	for a in range(0,len(ray1)):
		but([ray1[a]],0,0)
	pyautogui.keyUp("win")
	if len(ray2)>0:
		but(ray2,0,0)
inp = []
res2(inp)