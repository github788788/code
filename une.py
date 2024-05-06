exec(open('util.py').read())
def une(inp):
	dat = []
	for a in range(1,12):
		fil = "une"+str(a)
		tex = rea4([fil,"txt"])
		#print (tex)
		sta = "Transmission of material"
		end = "This news release presents"
		sta2 = tex.find(sta)
		end2 = tex.find(end,sta2)
		inf = tex[sta2:end2]
		day = inf.find("Technical information")
		day2 = inf[0:day]
		day2 = day2.replace("\n"," ")
		fri = day2.find("Friday")
		day2 = day2[fri:len(day2)]
		dayf = day2.replace("Friday, ","")
		#print (dayf)
		#continue
		#day3 = day2[day2.find("Friday"):len(day2)]
		#dayf = day3.replace("Friday, ","")
		rat = inf.find(" percent")
		rat2 = rat-10
		cen = inf[rat2:rat]
		cen = cen[::-1]
		cen = cen[0:cen.find(" ")]
		cen = cen[::-1]
		print(dayf,cen)
		dat.append([cen,dayf])
	pri(dat)
inp = []
une(inp)