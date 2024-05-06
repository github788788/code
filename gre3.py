exec(open('util.py').read())
def gre3(inp):
	dep =str(input("from = "))
	arr =str(input("to = "))
	mon =str(input("month = "))
	day =str(input("day = "))
	dat = mon+"/"+day+"/2020"


	neu("greyhound.com",2,7)
	cf_et2("from",0,1)
	wri(dep,2)
	but(["down","tab","tab"],0,3)
	wri(arr,2)
	"""
	but(["down","tab"],0,3)
	wri(dat,2)
	cf_este3(["search",0,0])
	"""

#def des(inp):

inp = []
gre3(inp)