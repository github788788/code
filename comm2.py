exec(open('util.py').read())
def comm2():
	#https://commonhelp.virginia.gov/access/			
	url = "https://commonhelp.virginia.gov/access/"
	usn = "medicaid67"
	pas = "Medmed1!"
	#inp.append([cf_et4(text)])	
	inp = []
	inp.append([neu3,[url,2,5]])
	inp.append([cf_este3,["check",0,5]])

	#inp.append([but3,[["tab"],0,1]])
	#inp.append([cf_et5,["account",1,1]])
	inp.append([usn])
	inp.append([but3,[["enter"],0,4]])
	inp.append([pas])
	inp.append([but3,[["enter"],0,0]])
	fof3(inp)

inp = []
comm2(inp)