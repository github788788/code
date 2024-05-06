exec(open('util.py').read())
def cal():

	hod3(["alt","tab",1,1])
	sw("cal.txt",2)
	hod3(["ctrl","a",1,0])
	hod3(["ctrl","c",1,0])
	hod3(["alt","f4",1,0])
	hod3(["ctrl","v",1,1])
	but(["tab","tab","tab","enter"],0,0)

	inp = []
cal(inp)