exec(open('util.py').read())
def to_percent(inp):
	val = inp*10000
	val = int(val)
	val = val/100
	val = str(val)+"%"
	return val
inp = []
to_percent(inp)