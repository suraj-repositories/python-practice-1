import smtplib  # (smtplib)simple mail transfer protocol library

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password123"
subject = "Python email test"
body = "I wrote an email :D"

# HEADER            
message = f"""From : {sender}
To : {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587) # 587 is the port number use for email
server.starttls()   # start tls = start transport layer security
try:
    server.login(sender,password)   # login to the server
    print("Logged in...")
    server.sendmail(sender, receiver,message)   # send emil
    print("Email has been sent !")

except smtplib.SMTPAuthenticationError:     # if fail the exception will occure
    print("unable to sign in !")