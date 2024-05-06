exec(open('util.py').read())
def gif(inp):
	import moviepy.editor as mp
	inp = inp
	#fol = os.getcwd()+"\\4tg"
	fol = os.getcwd()
	lis = os.listdir(fol)
	for a,val in enumerate(lis):
		if ".gif" in val:
			print (val)

			#
			old = val
			new = old.replace(".gif","2.mp4")

			clip = mp.VideoFileClip(old)
			clip.write_videofile(new)
			"""

			rep = val.replace(".gif",".mp4")
			if rep not in lis:
				print (a,val)
				beg = fol+"\\"+val
				end = fol+"\\"+rep
				clip = (VideoFileClip(beg))
				clip.write_gif(end,fps=15)
				"""


inp = []
gif(inp)