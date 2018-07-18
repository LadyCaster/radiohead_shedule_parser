#!/usr/bin/env python3
import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import waste

fromaddr = os.environ.get("FROMADDR", '')
toaddr = os.environ.get("TOADDR", '')
password = os.getenv("PASSWORD", '')
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Radiohead shedule'

body = waste.main(url=['http://www.wasteheadquarters.com/schedule/radiohead',
                       'http://www.wasteheadquarters.com/schedule/thom-yorke'])
msg.attach(MIMEText(body, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
