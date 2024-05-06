exec(open('util.py').read())
def dec(inp):
	num = inp[0]
	dep = inp[1]
	num = num*100
	num = int(num)
	num = num/100
	return num
inp = []
dec(inp)