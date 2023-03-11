import smtplib
from email.message import EmailMessage


def accident_emergency_email():
    # Please replace below with your email address and password
    # below given mail is my id . Don't use it.

    email_from = 'crashdetect108@gmail.com'
    password = 'fsbzhhwhwvfptbzq'

    # write the destination email id here in quotes.
    email_to = '####' 

    # mail content
    
    subject = 'ACCIDENT DETECTED'
    body = "Accident Detected with the help of CCTV fixed in this area . Immidiate emergency is needed .Send the help care immidiately "

    en = EmailMessage()
    en['From']=email_from
    en['To']=email_to
    en['Subject']=subject
    en.set_content(body)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
 
    # start TLS for security
    s.starttls()
 
    # Authentication
    s.login(email_from , password)
    
    # sending the mail
    s.sendmail(email_from,email_to, en.as_string())
 
    # terminating the session
    s.quit() 



   