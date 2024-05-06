exec(open('util.py').read())
def gif(inp):
	inp = inp
	#fol = os.getcwd()+"\\4tg"
	fol = os.getcwd()
	lis = os.listdir(fol)
	fil = "aoc"
	typ1 = "mp4"
	fil2 = fil+"."+typ1
	fil3 = fil+"."+"gif"
	#typ2 = "gif"
	beg = fol+"\\"+fil2
	end = fol+"\\"+fil3
	from moviepy.editor import VideoFileClip
	videoClip = VideoFileClip(fil2)
	videoClip.write_gif(fil3)
	dow = "E:\\Users\\-\\Downloads\\"
	out = dow+fil2.replace(".mp4",".gif")
	shutil.copy(fil2,out)


	#clip = (VideoFileClip(beg))
	#clip.write_gif(end,fps=15)
	"""
	for a,val in enumerate(lis):
		if ".mp4" in val:
			rep = val.replace(".mp4",".gif")
			if rep not in lis:
				print (a,val)
				beg = fol+"\\"+val
				end = fol+"\\"+rep
				clip = (VideoFileClip(beg))
				clip.write_gif(end,fps=15)
				"""


inp = []
gif(inp)