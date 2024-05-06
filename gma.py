exec(open('util.py').read())
def gma(inp):

	import smtplib
	 
	# list of email_id to send the mail
	#li = ["xxxxx@gmail.com", "yyyyy@gmail.com"]
	li = []
	li.append("media788788@gmail.com")
	li.append("desk788788@gmail.com")
	li.append("violin78@protonmail.com")
	li.append("cello34@protonmail.com")
	li.append("violin78@mail.com")
	li.append("usa2@email.com")


	for dest in li:
	    s = smtplib.SMTP('smtp.gmail.com', 587)
	    s.starttls()
	    s.login("media788788", "Medmed1!")
	    message = "Message_you_need_to_send"
	    s.sendmail("sender_email_id", dest, message)
	    s.quit()	
	    

	""" 
	for dest in li:
	    s = smtplib.SMTP('smtp.gmail.com', 587)
	    s.starttls()
	    s.login("sender_email_id", "sender_email_id_password")
	    message = "Message_you_need_to_send"
	    s.sendmail("sender_email_id", dest, message)
	    s.quit()	
	    """
	
inp = []
gma(inp)