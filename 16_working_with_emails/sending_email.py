import smtplib
from getpass import getpass
import imaplib

def send_email():
    smtp_object = smtplib.SMTP("smtp.gmail.com",587)
    smtp_object.ehlo()
    smtp_object.starttls()
    email = getpass("Please provide your mail id: ")
    passcode = getpass("Please enter your password: ")
    smtp_object.login(email,passcode)
    from_addr = email
    to_addr = email
    subject = input("Please enter email subject: ")
    message = input("Please enter email body: ")
    msg = "Subject: " + subject + "\n" + message
    print(smtp_object.sendmail(from_addr, to_addr, msg))
    smtp_object.close()


#flro kwex repy rlzv
def receive_email():
    imaplib_object = imaplib.IMAP4_SSL('imap.gmail.com')
    email = getpass('Please provide email: ')
    passcode = getpass('Please provide passcode: ')
    print(imaplib_object.login(email,passcode))
    imaplib_object.select("INBOX")
    typ,data=imaplib_object.search(None,'SUBJECT "Test Email"')
    result, email_data = imaplib_object.fetch(bytes(str(data[0]), 'utf-8'), '(RFC822)')
    print(email_data)


if __name__ == "__main__":
    # send_email()
    receive_email()
    
