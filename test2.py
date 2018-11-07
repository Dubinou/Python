import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
 
fromaddr = "v.dubernet@intech-sud.fr"
toaddr = "XXXXXXXX@intech-sud.fr"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Objet"
 
body = "Message"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(fromaddr, "JE VAIS T'ECLATER")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
