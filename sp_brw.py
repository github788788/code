exec(open('util.py').read())
def sp_brw(ray,ch,at):
	curr_file = os.path.basename(__file__)
	file = curr_file.replace(".py","")
	#file = "fl"
	file_xlsx = file+".xlsx"
	file_csv = file+".csv"
	workbook = xlsxwriter.Workbook(file_xlsx)
	worksheet = workbook.add_worksheet()
	too_long = []
	ray_csv = []
	urls = ray
	for a in range(0,len(urls)):
		if len(urls[a])<=256:
			 worksheet.write(a,0,urls[a])
			 ray_csv.append([urls[a]])
		else:
			fir = urls[a][0:255]
			sec = urls[a][255:len(urls[a])]
			ray_csv.append([fir,sec])
			worksheet.write(a,0,fir)
			worksheet.write(a,1,sec)
			too_long.append(a)
	workbook.close()
	#file_csv = file.replace(".xlsx",".csv")
	f = open(file_csv, 'wb')
	with f:
	    writer = csv.writer(f)
	    for row in ray_csv:
	        writer.writerow(row)
	if at==1:
		hod3(["alt","tab",1,0])
	#os.startfile(file_csv)
	if ch=="csv":
		os.startfile(file_csv)
	if ch=="xlsx":
		os.startfile(file_xlsx)
	time.sleep(3)
	hod3(["ctrl","home",1,0])
	for_length = len(urls)
	for a in range(0,for_length):
		hod3(["ctrl","c",1,0])
		hod3(["alt","tab",1,0])
		hod3(["ctrl","t",1,0])
		hod3(["ctrl","v",1,0])
		if a in too_long:
			hod3(["alt","tab",1,0])
			but(["right"],0,0)
			hod3(["ctrl","c",1,0])
			hod3(["alt","tab",1,0])
			hod3(["alt","d",1,0])
			#but(["right"],0,0)
			hod3(["ctrl","end",1,0])
			hod3(["ctrl","v",1,0])
		but(["enter"],0,0)
		if a<for_length-1:
			hod3(["alt","tab",1,0])
			but(["down"],0,0)
			if a in too_long:
				but(["left"],0,0)
		if a==for_length-1:
			hod3(["alt","tab",1,0])
			hod3(["alt","f4",1,1])

inp = []
sp_brw(inp)