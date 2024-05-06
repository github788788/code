exec(open('util.py').read())
def luf3():

	depart = str(input("depart = "))
	arrive = str(input("arrive = "))

	com = []
	com.append([neu3,["https://www.lufthansa.com/se/en/homepage",2,5]])
	com.append([init,["fof.txt"]])
	com.append([cf_et5,["hotel",1,0]])
	com.append(["cop",depart])
	com.append([but3,[["tab","tab"],0,1]])
	com.append(["cop",arrive])
	#com.append([but3,[["tab","space"],1,0]])
	com.append([cf_ests2,["one"]])
	#cf_ests2

	fof2(com)

	cf_este2("search flights",0)
inp = []
luf3(inp)