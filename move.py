exec(open('util.py').read())
def move(inp):
	
	cwd = os.getcwd()
	lis = os.listdir(cwd)
	file_to_move = "install_modules_compiled.cpython-37.pyc"
	other_drive_letter = "E"
	src = cwd+"\\"+file_to_move
	dst = src.replace("C:",other_drive_letter+":")
	dst = dst.replace("-","--")
	print(src)
	print(dst)
	#sye()
	shutil.copy(src,dst)
	
	
inp = []
move(inp)