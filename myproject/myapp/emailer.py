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
        self.smtp = smtplib.SMTP('smtp.gmail.com', 587) #server and port of your SMTP server
        self.smtp.ehlo() 
        self.smtp.starttls() 
        self.smtp.login('ACED.Tennis.Team@gmail.com', 'psmgnqwgvxaxzxou') #login email and password

    def sendEmail(self, text, subject, email):
        msg = MIMEMultipart() 
        msg['Subject'] = subject 
        msg.attach(MIMEText(text)) 
        self.smtp.sendmail(from_addr="Your Login Email", to_addrs=email, msg=msg.as_string()) 
        self.smtp.quit()

    def sendReservationConfirmation(self,res_id, email):
        subject = "ACED Reservation Confirmation"
        text = ("You scheduled a reservation!" + '\n'
                + "Reservation ID: " + str(res_id) +'\n'
                + "Please use the scheduler if you need to delete or change your reservation!")
        self.connect()
        self.sendEmail(text, subject, email)
        
#emailer testing (must have SMPTP server set up)
emailer = Emailer()
#emailer.connect()
#emailer.sendEmail("Hello World", "Test", "cookepoli@hartford.edu")
