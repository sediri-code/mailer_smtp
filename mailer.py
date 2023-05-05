import smtplib

def send_email(to, subject, body, sender_email, sender_password):
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()

    
    server.login(sender_email, sender_password)

    message = f'Subject: {subject}\n\n{body}'

    
    server.sendmail(sender_email, to, message)

    server.close()


to = 'recipient@example.com'
subject = 'Test email'
body = 'Hello, this is a test email!'
sender_email = 'sender@gmail.com'
sender_password = 'sender_password'

send_email(to, subject, body, sender_email, sender_password)
