exec(open('util.py').read())
def lan(inp):
	
	import win32api
	#win32api.LoadKeyboardLayout('00000401',1) # to switch to arabic
	#win32api.LoadKeyboardLayout('00000409',1) # to switch to english
	#win32api.LoadKeyboardLayout('00000401',1) # to switch to english 

	print (win32api.GetKeyboardLayoutList())

	print (win32api.GetKeyboardLayout())

	print (win32api.GetKeyboardLayoutName())

	lan1 = "67699721"
	lan2 = "69010461"
	lan3 = "67175425"
	lan4 = "00000409"

	#win32api.LoadKeyboardLayout(lan4,1) # to switch to english
	win32api.LoadKeyboardLayout('00000401',1) # to switch to arabic
	"""
	(67699721, 69010461, 67175425)
	67699721
	00000409
	"""

	#GetKeyboardLayoutName


	#GetKeyboardLayout

	"""
	00000409
	0000041d
	"""

	#Public Const LANG_SWEDISH = &H1D
	#win32api.LoadKeyboardLayout('00000401',1)

inp = []
lan(inp)