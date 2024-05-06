exec(open('util.py').read())
def ud(st):
	st = st[::-1]
	fi = st.find("\\")
	st = st[fi+1:len(st)]
	st = st[::-1]
	print(st)
	return st
inp = []
ud(inp)