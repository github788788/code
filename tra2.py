exec(open('util.py').read())
def tra2(inp):
	alt(1,1)
	for a in range(0,11):
		hod3(["ctrl","pagedown",1,1])
		var = 11-a
		nam = "une"+str(var)+".txt"
		hod3(["ctrl","a",1,1])
		hod3(["ctrl","c",1,1])
		sw("wordpad.exe",1)
		hod3(["ctrl","v",1,1])
		hod3(["ctrl","s",1,1])
		loc = "E:\\Users\\-\\cod"+"\\"+nam
		wri(loc,1)
		key([["enter",2,1,0]])
		af4(1,1)
	
	


inp = []
tra2(inp)