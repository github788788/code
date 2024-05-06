exec(open('util.py').read())
def luf2():

	depart = str(input("depart = "))
	arrive = str(input("arrive = "))

	com = []
	com.append([neu3,["https://www.lufthansa.com/se/en/homepage",2,5]])
	com.append([cf_et5,["hotel",1,1]])
	#com.append(["cop",depart])
	com.append([wri3,[depart,2,1]])
	#neu("https://www.lufthansa.com/se/en/homepage",2,5)
	#cf_et3("hotel",1,2)
	#wri(depart,1)
	com.append([but3,[["tab","tab"],1,0]])
	#but(["tab","tab"],1,0)
	#com.append(["cop",arrive])
	com.append([wri3,[arrive,2,1]])
	#wri(arrive,1)
	#but(["tab","space"],0,1)
	com.append([but3,[["tab","space"],1,0]])
	fof2(com)

	cf_este2("search flights",0)
inp = []
luf2(inp)