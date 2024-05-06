exec(open('util.py').read())
def szt(inp):
	cwd = os.getcwd()
	out = cwd+".7z"
	print (cwd,out)
	with py7zr.SevenZipFile(out, 'w') as archive:
		    archive.writeall(cwd)
inp = []
szt(inp)