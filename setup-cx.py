exec(open('util.py').read())
def cx(inp):

	from cx_Freeze import setup, Executable

	setup(

		name="YourAppName",

		version="1.0",

		description="Your application description",

		executables=[Executable("stock4.py")],

	)   
	"""
	import cx_Freeze, sys
	base = None
	if sys.platform == 'win32':
	    base = "Win32GUI"
	executables = [cx_Freeze.Executable("util.py", base=base, targetName="util")]
	cx_Freeze.setup(
	    name="util",
	    options={"build_exe": {"packages": ["tkinter"], "include_files": [
	        "someImage.png", "anotherImage.png",
	    ]}},
	    version="1.0",
	    description="mah file",
	    executables=executables
	)
	"""
	
inp = []
cx(inp)