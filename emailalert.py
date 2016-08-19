import smtplib,pdb
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from authentication import *

def email_user_alert(message,subject_line,html_file):
    msg = MIMEMultipart('alternative')
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login(EMAIL_ACCOUNT,EMAIL_PASSWORD)
    msg['Subject'] = subject_line
    msg['From'] = EMAIL_ACCOUNT
    msg['To'] = EMAIL_ACCOUNT_MAIN
    body_message = MIMEText(message, 'plain')
    msg.attach(body_message)
    with open(html_file, 'r') as html_file:
        attachment = MIMEText(html_file.read())
        attachment.add_header('Content-Disposition', 'attachment', filename="newsletter.html")
        msg.attach(attachment)

    mail.sendmail(EMAIL_ACCOUNT,EMAIL_ACCOUNT_MAIN,msg.as_string())
    mail.close()
