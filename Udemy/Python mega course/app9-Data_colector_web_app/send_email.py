from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
	from_email = "lucas27_olivio@hotmail.com"
	from_pass = "B53b271fa3()"
	to_email = email

	subject = "Height data"
	message = "Hey there, your height is <strong>%s</strong>.<br>Average height of all is <strong>%s</strong>.<br>Total participants: <strong>%s</strong>.<br><br>Thanks for participating!"%(height, average_height, count)

	msg = MIMEText(message, 'html')
	msg['Subject'] = subject
	msg['To'] = to_email
	msg['From'] = from_email

	hotmail = smtplib.SMTP('smtp-mail.outlook.com',587)
	hotmail.ehlo()
	hotmail.starttls()
	hotmail.login(from_email, from_pass)
	hotmail.send_message(msg)