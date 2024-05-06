exec(open('util.py').read())
def amt2():
	inp = []
	inp.append("depart")
	inp.append("arrive")
	inp.append("month")
	inp.append("day")
	inp = ask(inp)

	dep = inp[0][1]
	arr = inp[1][1]
	mon = inp[2][1]
	day = inp[3][1]

	dat = mon+"/"+day+"/2020"

	ray = []
	ray.append([neu3,["amtrak.com",1,13]])
	ray.append([cf_e2,["use p"]])
	ray.append([but3,[["tab","tab"],0,1]])
	ray.append([dep])
	ray.append([but3,[["tab","tab","tab"],0,1]])
	ray.append([arr])
	ray.append([but3,[["tab","tab"],0,1]])
	ray.append([dat])
	ray.append([cf_este3,["find t",0,0]])
	fof3(ray)


	"""
	inp.append([[ski],[neu,["https://www.amtrak.com/home.html",1,20]]])
	inp.append([[ski],[cf_e,["use p"]]])
	inp.append([[ski],[but,[["tab","tab"],0,1]]])
	inp.append([["from"],[but,[["tab","tab"],0,1]]])
	inp.append([["to"],[but,[["tab"],0,1]]])
	inp.append([["month"]])
	inp.append([["day"]])
	inp.append([[ski],[wri,[dat,1]]])
	inp.append([[ski],[cf_este3,["find t",0,0]]])
	inp = inv(inp,ski)
	mat = []
	mat.append("month")
	mat.append("day")
	mat = mkr(mat)
	mat = gev(inp,mat)
	mon = mat[0][1]
	day = mat[1][1]
	dat = mon+"/"+day+"/2020"
	rev = []
	rev.append(["__dat__",dat])
	inp = rep([inp,rev])
	mo2 =gef([inp,ski])
	dr(mo2)
	rum([mo2])
	"""
inp = []
amt2(inp)