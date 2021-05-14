#!/usr/bin/python3
import smtplib

#https://www.tutorialspoint.com/python3/python_sending_email.htm


sender = 'incyt@url.edu.gt'
subject = ''
receivers = []

html_format = "MIME-Version: 1.0\nContent-type: text/html\nSubject: SMTP HTML e-mail test\n"


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
    subject = readSubject()
    for receiver in receivers:
        print("*************************************************************")
        try:
            
            message = str(f"From: Incyt URL <{sender}>\nTo: <{receiver}>\nSubject: {subject}\n{bodyMessage}").encode("ascii", "replace")
            print(message)
            smtpObj = smtplib.SMTP('smtpdti.url.edu.gt')
            smtpObj.sendmail(sender, receiver, message)
            print ("Successfully sent email")
        except:
            print ("Error: unable to send email")


if __name__ == "__main__":


    readBodyMessage()
    readReceivers()
    sendMessages()
    print('end of process')
