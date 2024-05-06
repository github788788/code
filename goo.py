exec(open('util.py').read())
def goo(inp):
	#"os.rename(old, new)"
	#"E:\\Program Files (x86)\\Google\\Update"

	fol = "E:\\Program Files (x86)\\Google\\Update"
	lis = os.listdir(fol)

	gon = ["Update","update"]
	for a,val in enumerate(lis):
		if "Update" in val:
			old = fol+"\\"+val
			new = fol+"\\"+val.replace("pdate","nein")
			#new = old.replace(val,"nein")
			print (old)
			os.rename(old, new)
			#shutil.copy(old,new)

		cou = val.count(".")
		if cou>1:
		#if "." in val:
			fol2 = fol+"\\"+val+"\\"
			print (fol2)
			lis2 = os.listdir(fol2)
			#print(lis2)
			for b,val2 in enumerate(lis2):
				#print(val2)
				if "Update" in val2:
					old = fol2+"\\"+val2
					print(old)
					new = fol2+"\\"+val2.replace("pdate","nein")
					#new = old.replace(val,"nein")
					print (new)
					os.rename(old, new)



	


		#print (cur)
		"""
 

	ori = "E:\\Program Files (x86)\\Google\\Update\\GoogleUpdate.exe"


	old = "GoogleUpdate"
	new = "nein"
	old = fol+"\\"+
	"""


inp = []
goo(inp)