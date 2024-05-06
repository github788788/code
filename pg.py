exec(open('util.py').read())
def pg(li):
	pu(len(li)-1)
	le = 0
	for a in range(0,len(li)):
		 if "google.com/flights" in li[a]:
		 	le = le+1
	for a in range(0,le):
		cf_etste("price graph")
		if a<le-1:
			hod3(["ctrl","pagedown",1,0])

inp = []
pg(inp)