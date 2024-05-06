exec(open('util.py').read())
def but3(inp):

	ray = inp[0]
	between_wait = inp[1]
	end_wait = inp[2]	

	for a in range(0,len(ray)):
		pyautogui.press(ray[a])
		time.sleep(between_wait)
	time.sleep(end_wait)

inp = []
but3(inp)