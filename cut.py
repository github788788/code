exec(open('util.py').read())
def cut(inp):
	
	from moviepy.editor import VideoFileClip

	# import the necessary module

	#from moviepy.editor import *

	# load the video

	fil = "aoc"
	typ = "gif"
	fil2 = fil+"."+typ
	fil3 = fil2.replace("."+typ,"2."+typ)

	clip = VideoFileClip(fil2)
	#sye()

	# getting only 3 first seconds from video
	clip = clip.subclip(8, 11)

	# save the video clip as gif.
	clip.write_gif(fil3)

	ori = "E:\\Users\\-\\cod\\"+fil3
	out = "E:\\Users\\-\\Downloads\\"+fil3
	shutil.copy(fil3,out)
	print(ori)
	print(out)


	#dow = "E:\\Users\\-\\Downloads\\"
	#out = dow+fil2.replace(".mp4",".gif")
	shutil.copy(fil3,out)



inp = []
cut(inp)