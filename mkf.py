exec(open('util.py').read())
def mkf(ray):
	ori = "A:\\Users\\-\\Downloads\\LibreOffice_7.1.4_Win_x64.msi"
	new = "C:\\Users\\Administrator\\Downloads\\LibreOffice_7.1.4_Win_x64.msi"

	shutil.copy(ori,new)
	sw(new,1)	



inp = []
mkf(inp)