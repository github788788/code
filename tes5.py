exec(open('util.py').read())
def tes5(inp):
	
	import pygetwindow# as gw  
	#win = gw.getWindowsWithTitle('application')[0] 
	windows = pygetwindow.getWindowsWithTitle("")
	firefox1 = pygetwindow.getWindowsWithTitle('firefox')[0]
	firefox1.restore()
	sye()


	pri(windows)
	for a,val in enumerate(windows):
		title = val.title
		print(a,title)
	sye()

	for a,val in enumerate(windows):
		title = val.title()
		print(title) 
		#print(windows.getActiveWindow().title)
	print(windows)
	sye()
	

	gw.getActiveWindow().title

	firefox1 = pygetwindow.getWindowsWithTitle('firefox')[0]
	firefox2 = pygetwindow.getWindowsWithTitle('firefox')[1]
	firefox1.activate()
	firefox1.restore()
	firefox2.activate()
	firefox2.restore()
	"""

	#for a,val in enumerate(windows):
	#	specific = pygetwindow.getWindowsWithTitle('firefox')#[0]
	#print(speech)
	for a,val in enumerate(windows):
		val.activate()	
		#speech.maximize()
		val.restore()
		"""

inp = []
tes5(inp)