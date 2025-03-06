from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart 
import smtplib 
import os

class Emailer:
    def __init__(self):
        self.smtp = None

    def connect(self):
        self.smtp = smtplib.SMTP('smtp.gmail.com', 587) 
        self.smtp.ehlo() 
        self.smtp.starttls() 
        self.smtp.login('ACED.Tennis.Team@gmail.com', 'psmgnqwgvxaxzxou') 

    def sendEmail(self, text, subject, email):
        msg = MIMEMultipart() 
        msg['Subject'] = subject 
        msg.attach(MIMEText(text)) 
        self.smtp.sendmail(from_addr="Your Login Email", to_addrs=email, msg=msg.as_string()) 
        self.smtp.quit()

emailer = Emailer()
emailer.connect()
emailer.sendEmail("Hello World", "Test", "jhart@hartford.edu")