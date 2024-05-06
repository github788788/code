exec(open('util.py').read())
def tid(inp):
	import datetime
	dat = "2022-10-15"
	dat2 = datetime.datetime.strptime(dat,'%Y-%m-%d')
	las = dat2-datetime.timedelta(1)
	cur = las.strftime("%m.%d.%Y")

	print (las,cur)
	

	"""

	today = datetime.date.today()
	#day = today.weekday()
	#dat2 = datetime.datetime.strptime(dat,'%b %d, %Y')
	las = today-datetime.timedelta(1)
	print (today,las)
	"""

inp = []
tid(inp)