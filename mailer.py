import smtplib

def send_email(to, subject, body, sender_email, sender_password):
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(sender_email, sender_password)
    
    