exec(open('util.py').read())
def find_click(find,end_wait):
	hod3(["ctrl","f",1,1])
	wri(find,1)
	but(["esc","enter"],0,end_wait)inp = []
find_click(inp)