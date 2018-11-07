#!/usr/bin/python

import ssl
import OpenSSL
import datetime
import smtplib

cert = ssl.get_server_certificate(('www.google.com', 443))

# OpenSSL
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
print(x509.get_subject().get_components())

date = x509.get_notAfter()

print(datetime.datetime.strptime(date.decode('ascii'), '%Y%m%d%H%M%SZ'))

import smtplib

SERVER  = "smtp-mail.outlook.com"
PORT    = 587
USER    = "v.dubernet@intech-sud.fr"
PASS    = ""
FROM    = USER
TO      = ["a.criblez@intech-sud.fr"]
SUBJECT = "Hey petit !"
MESSAGE = "Salut YOYO YO YO YO YYOYOYO"

mailserver = smtplib.SMTP('smtp.office365.com',587)
mailserver.ehlo()
mailserver.starttls()
mailserver.login(USER, PASS)
mailserver.sendmail(USER,TO,MESSAGE)
mailserver.quit()
