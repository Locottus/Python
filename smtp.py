#!/usr/bin/python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#https://www.tutorialspoint.com/python3/python_sending_email.htm
#https://www.javacodemonk.com/send-rich-text-multimedia-email-in-python-d21c900f

sender = 'incyt@url.edu.gt'
subject = ''
receivers = []

#html_format = "MIME-Version: 1.0\nContent-type: text/html\nSubject: SMTP HTML e-mail test\n"


def readReceivers():
    print('reading receivers')
    f = open('correos.txt', 'r')  
    mails = f.readlines()
    for mail in mails:
        if (len(mail) > 4):
            print(mail)
            receivers.append(str(mail).replace("\n", ""))
    print(len(receivers))


def readBodyMessage():
    print('reading body')
    f = open('mensaje.txt', 'r')  
    bodyMessage = str(f.read())
    return bodyMessage
    
def readSubject():
    print('reading subject')
    f = open('subject.txt', 'r')  
    s = str(f.read())
    return s


def sendMessages():
    print('sending emails')
    bodyMessage = readBodyMessage()
    print(bodyMessage)
    subject = readSubject()
    for receiver in receivers:
        print("*************************************************************")
        try:
            msg = MIMEMultipart()
            print(receiver)
            msg['From'] = sender
            msg['To'] = receiver
            msg['Subject'] = subject
            msg.attach(MIMEText(bodyMessage, 'plain'))
            #msg.attach(MIMEText(bodyMessage, 'html')) #to send html messages
            text = msg.as_string()

            smtpObj = smtplib.SMTP('smtpdti.url.edu.gt')
            smtpObj.sendmail(sender, receiver, text)
            print ("Successfully sent email")
            smtpObj.quit()
        except:
            print ("Error: unable to send email")



if __name__ == "__main__":

    readReceivers()
    sendMessages()
    print('end of process')
