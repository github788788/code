exec(open('util.py').read())
def ren(inp):
	#cwd = os.getcwd()+"\\ren\\"
	cwd = os.getcwd()+"\\"
	lis = os.listdir(cwd)
	rep = []
	rep.append(["-inf",".3"])
	#rep.append(["med.2","med.02"])
	#rep.append([".6",".06"])
	#rep =["med.1","med.2"]
	#rep = ""
	for a, val in enumerate(lis):
		for b, val2 in enumerate(rep):
			ide =val2[0]
			if ide in val:
				old = cwd+val
				cha = val2[1]
				new = old.replace(ide,cha)
				shutil.copy(old,new)
				print (old,new)
				#os.remove(old)
				"""
				new = val2[1]
				#new = old.replace(val,new)
				nam = val.replace(ide,new)
				new2 = cwd+nam
				shutil.copy(src, dst)
				"""

				#os.rename(old, new2)#
				#inp = []

cwd = os.getcwd()
inp = [cwd]
ren(inp)