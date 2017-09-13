#!/usr/bin/python

import os, sys, smtplib

header = "Subject: hello from Dogmail\nFrom:noreplay@dogmail.cloudapp.net\nTo:"
def correo(receivers):
    print "entrando a correo"

    sender = 'herlich@dogmail.cloudapp.net'
    #receivers = ['herlich@dogmail.cloudapp.net']

    message = header + receivers + """

    This is a test e-mail message.
    this email was sent using Python
    Hello world!
    best regards,
    Herlich Gonzalez
    """
    try:
       smtpObj = smtplib.SMTP('localhost', 25)#smtplib.SMTP()
       smtpObj.sendmail(sender, receivers, message)
       smtpObj.quit()
       print "Successfully sent email"
    except:
       print "Error: unable to send email"

#main
print "inicia programa de enviar correos"
correo('herlich@gmail.com')
correo('herlich@dogmail.cloudapp.net')
correo('herlich.gonzalez@xerox.com')
correo('heizel.gonzalez@xerox.com')
print "final del programa"
