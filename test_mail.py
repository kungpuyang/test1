import smtplib # SMTP protocol client
import ssl # Secure Sockets Layer
from email.mime.text import MIMEText # MIMEText class
from email.mime.multipart import MIMEMultipart # MIMEMultipart class
from email.header import Header # Header class

sender = 'kungpuyang@gmail.com'
receiver = ['kungpuyang@yahoo.com','111240677@webmail.nou.edu.tw']
passwd = 'uwkn hgpm ktdg jygz'

for i in receiver:
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = i
    msg['Subject'] = Header('Test Email', 'utf-8').encode()

    body1 = 'This is a test email.\n'
    body2 = 'How are you?\n\n'
    body3 = 'Best regards,\n'
    body4 = 'Kung-Pu Yang' # 或是從檔案讀取而來！可以讀Markdown格式。

    msg_text = MIMEText(body, 'plain', 'utf-8')
    msg.attach(msg_text)
    c = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=c) as server:
        server.login(sender, password=passwd)
        server.sendmail(sender, i, msg.as_string())
    print('Email sent successfully.')




# with open('password.txt') as f:
#     f.writeline('password')