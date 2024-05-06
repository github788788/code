exec(open('util.py').read())
def env(inp):

	key = "Path"
	user = os.environ[key]

	new = "E:\\cygnus\\cygwin-b20\\H-i586-cygwin32\\bin"
	os.environ[key] = new
	#print(user)
	"""
	var = os.getenv(key)
	print(var)

	
	#var2 = os.putenv(key,new)
	#os.putenv(new,key)
	# os.putenv(key, value, /)
	# os.getenv(key, default=None)Â¶
	#os.environ.setdefault('USER_2', 'True')
	#var2 = os.environ.setdefault(key, new)

	#os.environ['USER_1'] = 'username'
	os.environ[key] = new
	#os.environ.setdefault[key] = new
	os.environ.setdefault(key, new)


	print("")
	var = os.getenv(key)
	print(var)
	"""

	user = os.environ[key]
	print(user)


inp = []
env(inp)