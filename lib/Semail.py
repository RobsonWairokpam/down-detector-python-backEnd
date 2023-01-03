import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_email(filename):
    mail_from = 'nehru.wairokpam@lamzing.com'
    mail_to = 'micky.rajkumarlamzing@gmail.com'
    # mail_to = ['micky.rajkumarlamzing@gmail.com','rajesh.lamzing@gmail.com','nehru.wairokpam@lamzing.com','ailan.maibam@lamzing.com']
    mail_to = ['micky.rajkumarlamzing@gmail.com','sumanyumnam.lamzing@gmail.com']

    msg = MIMEMultipart()
    msg['From'] = mail_from
    #msg['To'] = mail_to
    msg['To'] = ", ".join(mail_to)
    msg['Subject'] = 'Gov Website Report'
    mail_body = "Gov Website Report"

    msg.attach(MIMEText(mail_body))

    filename= filename
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)


    try:
        server = smtplib.SMTP_SSL('smtp.sendgrid.net', 465)
        server.ehlo()
        server.login('apikey', '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')
        server.sendmail(mail_from, mail_to, msg.as_string())
        server.close()
        print("mail sent")
    except:
        print("issue")
        server.close()


