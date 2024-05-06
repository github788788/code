exec(open('util.py').read())
def login(username,pw,end_wait):
	wri(username,1)
	but(["tab"],1,0)
	wri(pw,1)
	but(["enter"],0,end_wait)
inp = []
login(inp)