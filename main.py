from smtp_client import ICloudMail
from message_builder import create_message
from email import policy
from Message_parser import parse_message
 
EMAIL = input("enter your email:")
PASSWORD = input("enter your password"
)
test_send = input("do you want to send a test email? Y/N:")

if test_send.upper() == "Y":
    message = create_message(
         sender=EMAIL,
         to=[
           #REDACTED
        
             ],
             subject="test",
             text="if im seeing this im stupid and am too lazy to add my own input functions. screw you previous ben"
            )
    client = ICloudMail(
        EMAIL,
        PASSWORD
    )
    client.send(message)

    print("sent!")

from getpass import getpass
from Imap_client import ICloudMailIMAP

email = input("enter your email:")
password = input("enter your password:")

mail = ICloudMailIMAP(email, password)

try:
    mail.connect()
    count = mail.select_inbox()
    print("connected!")
    print(f"Number of messages in inbox: {count}")
    messages = mail.select_inbox()

    print("connected!")
    print(f"number of messages fetched : {count} ")

    messages = mail.fetch_latest(10)

    for raw_email in messages:
        print("DEBUG TYPE:", type(raw_email))
        msg = parse_message(raw_email)


        print("-----------------")
        print("from:", msg.get("from"))
        print("Subject:", msg.get("Subject"))
        print("Date:", msg.get("Date"))
        print(msg.get("body"))
finally:
    mail.disconnect()
