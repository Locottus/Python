#!/usr/bin/python3
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

#https://www.tutorialspoint.com/python3/python_sending_email.htm
#https://www.javacodemonk.com/send-rich-text-multimedia-email-in-python-d21c900f


sender = 'Incyt <incyt@url.edu.gt>'
subject = ''
receivers = []

regexEmail = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

def checkEmail(email):
    if(re.search(regexEmail, email)):
        print("Valid Email",email)
        return True
    else:
        print("Invalid Email",email)
        return False


def readReceivers():
    print('reading receivers')
    dataFile = pd.read_csv('correos.csv', header=0, sep=',', encoding = "ISO-8859-1", error_bad_lines=False, index_col=False, dtype='unicode')
    df = pd.DataFrame(dataFile)
    for index, row in df.iterrows():
        #print(row)
        mail = str(row[1]).replace("\n", "").replace("\t", "").replace(" ", "")
        if (checkEmail(mail)):
            receivers.append(str(row[0]).replace("\n", "") + ' <' +  mail + '>')
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
    print('end of line')
