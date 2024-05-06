exec(open('util.py').read())
def spe(inp):




	import pygetwindow# as gw  
	#win = gw.getWindowsWithTitle('application')[0] 	
	speech = pygetwindow.getWindowsWithTitle('chrome')[0] 
	speech.activate()	
	#speech.maximize()
	speech.restore()
	time.sleep(1)
	#speech.topleft(683,0)
	speech.topleft(683,0)
	#1366x768
	speech.bottomright(1366,768)

	sye()
	time.sleep(2)

	import pyautogui
	logo_location = pyautogui.locateOnScreen('logo.png')
	print(logo_location)
	pyautogui.moveTo(logo_location[0]-140,logo_location[1]+30)
	pyautogui.click()


	notepadWindow.minimize()


	#click_logo(["microphone3.png"])
	"""
	import numpy as np 
	import cv2 
	url = "https://www.investing.com/earnings-calendar/"
	#num5([url,2])
	#num6([url,7,1])
	screenshot_name = "screenshot.png"
	#screenshot_location = earn_folder+"\\"+screenshot_name
	screenshot = pyautogui.screenshot() 
	screenshot = cv2.cvtColor(np.array(screenshot), 
	                     cv2.COLOR_RGB2BGR) 
	cv2.imwrite(screenshot_name, screenshot) 
	logo_name = "microphone2" 
	#file_name = "logo"
	logo_file =logo_name+".png"
	#logo_location = earn_folder+"\\"+logo_file
	#match = logo_name+".png"
	location = pyautogui.locateOnScreen(logo_file)
	print(location)
	sye()	
	#print(location)
	pyautogui.moveTo(location[0],location[1])
	pyautogui.click()
	time.sleep(2)
	"""


inp = []
spe(inp)