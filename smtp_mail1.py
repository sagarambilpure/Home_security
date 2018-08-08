import smtplib
import imghdr
from email.message import EmailMessage
smtpUser = 'sagarraspproject@gmail.com'
smtpPass = 'sagarrasp'

toAdd = "sagarambilpure@gmail.com"
fromAdd= smtpUser

def sendPhoto():

    msg = EmailMessage()
    msg['From'] = smtpUser
    msg['To'] = toAdd
    msg['Subject'] ='Python Test'


    filePath = "image1.jpg"


    fp = open(filePath, 'rb')
    part = fp.read()
    fp.close()
    msg.add_attachment(part, maintype='image',subtype=imghdr.what(None, part))

    s= smtplib.SMTP('smtp.gmail.com',587)

    #s.ehlo()
    s.starttls()
    #s.ehlo()

    s.login(smtpUser,smtpPass)

    s.sendmail(fromAdd, toAdd,msg.as_string())

    s.quit() 
