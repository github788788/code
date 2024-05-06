exec(open('util.py').read())
def ge4(inp):
	inp = inp
	you =str(input("youtube mp4 url = "))
	tex = []
	tex.append(you)
	url = []
	#url.append("https://yt5s.com/en62/youtube-to-mp4")
	url.append("https://y2mate.is/en87/youtube-to-mp4.html")
	#https://www.youtube.com/watch?v=zGBWkWkOFxI
	num4([url,1])
	cfb(["converter",[["esc",1,0,1],["tab",1,0,1]]])
	cop([tex,0])
	#nex = tex([you,0])
	time.sleep(3)
	cfb(["720",[["esc",1,0,1],["tab",1,0,1],["enter",1,0,3]]])
	key([["tab",1,0,1],["enter",1,0,3],["enter",1,0,1]])
	hod3(["ctrl","f4",1,1])

	#fol = "B:\\Users\\-\\Downloads"

	fol = upd([1])+"Downloads"

	lis = os.listdir(fol)

	rep = "Y2Mate.is - "
	for a, val in enumerate(lis):
		if rep in val:
			old = fol+"\\"+val
			nam = val.replace(rep,"")
			new = fol+"\\"+nam
			os.rename(old, new)
		

		"""
		old = fol+"\\"+"document.pdf"
		nam = dat.replace("/",".")
		new = fol+"\\"+"med."+nam+".pdf"
		os.rename(old, new)
		"""	


from moviepy.editor import *
inp = []
ge4(inp)