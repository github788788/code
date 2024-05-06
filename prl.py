exec(open('util.py').read())
def prl(new,ray):
	new = int(new)
	usn = ray[0]
	pas = ray[1]
	if new==1:
		neu("https://mail.protonmail.com/login",1,5)
	login(usn,pas,1)
	"""inp = []
prl(inp)