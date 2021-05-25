#!/usr/bin/python3
import smtplib, re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd


receivers = []

regexEmail = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def checkEmail(email):
    if(re.search(regexEmail, email)):
        #print("Valid Email",email)
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



if __name__ == "__main__":
    readReceivers()
