#exec(open('util.py').read())
def ren3(inp):
	import os
	cwd = os.getcwd()
	lis = os.listdir(cwd)
	for a,val in enumerate(lis):
		if "une" in val:
			if ".html" in val:
				if "-" in val:
					old = val
					new = old.replace("-","")
					os.rename(old, new)
inp = []
ren3(inp)