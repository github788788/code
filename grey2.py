exec(open('util.py').read())
def grey2():
	inp = []
	inp.append("depart")
	inp.append("arrive")
	inp.append("month")
	inp.append("day of month")
	inp = ask(inp)
	dep = inp[0][1]
	arr = inp[1][1]
	mon = inp[2][1]
	day = inp[3][1]
	dat = mon+"/"+day+"/2020"
	com = []
	com.append([neu3,["greyhound.com",1,5]])
	#com.append([neu3,["greyhound.com",1,10]])
	#com.append([cf_et2,["from",1,1]])
	#com.append([cf_et2,["from"]])

	com.append([cf_et5,["from",1,1]])
	
	#cf_et5(inp)

	#com.append(["cop",dep])
	#com.append([wri3,[dep,1,1]])
	com.append([dep])
	#com.append([but3,[["down","enter","tab","tab"],0,1]])
	com.append([but3,[["down","tab","tab"],0,1]])
	#com.append(["cop",arr])
	com.append([arr])
	#com.append([but3,[["down","enter","tab"],0,1]])
	com.append([but3,[["down","tab"],0,1]])
	#com.append(["cop",dat])
	com.append([dat])
	com.append([cf_este3,["search",0,0]])
	fof3(com)
inp = []
grey2(inp)