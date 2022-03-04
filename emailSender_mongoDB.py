# Sarthak Gupta
# 1/11/2021
# Send HTML email with MIME using Python 3 from Mongo DB

import smtplib, ssl, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from pymongo import MongoClient

class Connect(object):
	@staticmethod    
	def get_connection():
		return MongoClient("mongodb://m001-student:m001-mongodb-basics@sandbox-shard-00-00.70xfj.mongodb.net:27017,sandbox-shard-00-01.70xfj.mongodb.net:27017,sandbox-shard-00-02.70xfj.mongodb.net:27017/ewb-asu?replicaSet=atlas-14k7o4-shard-0&authSource=admin&ssl=true")

subscribed_emails = []

connection = Connect.get_connection()
db = connection.ewb_asu
collection = db.members
for member in collection.find():
	if (member['subscribed']==True):
		subscribed_emails.append(member['email'])

print(subscribed_emails)

# emails_list = db.members.find_one({},{"email":1})
# print(emails_list)

port = 465 # for SSL
smtp_server = "smtp.gmail.com"

sender_email = getpass.getEmail()
sender_password = getpass.getpass()

receiver_email = "sarthakkgupta@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = 'EWB Newsletter'
message["From"] = sender_email
message["To"] = receiver_email

text = """\
INSERT EMAIL NEWSLETTER SUBJECT
"""
html = """\
<html>
INSERT HTML TEXT here
</html>
"""

# Turn these into MIMEtext objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	try:
		server.login(sender_email, sender_password)
	except:
		print('Incorrect password')
	try:
		# Send email here
		server.sendmail(sender_email, receiver_email, message.as_string())
		print('Email sent to ' + receiver_email + '.')
		#for subscriber in subscribed_emails:
		#	server.sendmail(sender_email, subscriber, message.as_string())
		#	print('Email sent to ' + subscriber + '.')
	except:
		print("Error.")
	
