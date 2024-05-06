#exec(open('util.py').read())
import os
def imp(inp):
	inp = inp
	#xlrd,pyautogui,xlwt,xlsxwriter,pandas
	ray = []
	#ray.append("python -m pip install --upgrade pip")
	ray.append("xlrd")
	ray.append("pyautogui")
	ray.append("xlwt")
	ray.append("xlsxwriter")
	ray.append("pandas")
	ray.append("py7zr")
	ray.append("flask")
	for a,val in enumerate(ray):
		command = "conemu.lnk"
		os.system(command)
		time.sleep(1)
		command = "cd code"
		os.system(command)
		#command = val
		if "python" not in val:
			command = "pip uninstall "+str(val)
		os.system(command)
		#os.system("pip install "+val[1])


	#os.system("pip install xlrd")		
inp = []
imp(inp)