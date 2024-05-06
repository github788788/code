exec(open('util.py').read())
def cpp(inp):
	"""
	https://www3.cs.stonybrook.edu/~alee/g++/g++.html
	https://www.tutorialspoint.com/How-to-compile-and-run-the-Cplusplus-program
	in terminal write "g++ to compile"
	then default file is a.exe, just type
	"a" or "a.exe" to run
	g++ -o wor wor.cpp
	g++ wor.cpp
	"""
	"""
	tex = "g++ -o wor wor.cpp"
	wri3([tex,2])
	key([["enter",1,0,2]])
	tex2 = "wor.exe"
	wri3([tex,1])
	key([["enter",1,0,0]])

	g++ -o wor wor.cpp
	"""
	#old gpl = "E:\\cygnus\\cygwin-b20\\H-i586-cygwin32\\bin"
		
	import subprocess
	gpf = "vcpkg.exe"
	gpd = "E:\\Program Files\\Git\\vcpkg"
	gpl = gpd+"\\"+gpf
	#fil = "wor2"
	fil =str(input("file = "))
	cod = fil+".cpp"
	sav = fil+".exe"
	print("compiling file "+cod+" to file "+sav)
	subprocess.run([gpl,cod,"-o",sav])
	"""
	input = input
	open conemu "E:\\Program Files\\ConEmu\\ConEmu64.exe"
	write "cd E:\\Program Files\\Git\\vcpkg"
	write" vcpkg install "+input
	"""
	
inp = []
cpp(inp)t