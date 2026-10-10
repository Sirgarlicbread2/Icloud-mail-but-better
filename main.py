from smtp_client import ICloudMail
from message_builder import create_message
from Message_parser import parse_message
from Imap_client import ICloudMailIMAP

EMAIL = input("enter your email: ").strip()
PASSWORD = input("enter your password: ").strip()

test_send = input("do you want to send a test email? Y/N: ").strip().upper()

if test_send == "Y":
    recipient = input("enter recipient email: ").strip()
    message = create_message(
        sender=EMAIL,
        to=[recipient],
        subject="test",
        text="If I'm seeing this, then I am too lazy to add my own input functions.",
    )
    client = ICloudMail(EMAIL, PASSWORD)
    client.send(message)
    print("sent!")

mail = ICloudMailIMAP(EMAIL, PASSWORD)

try:
    mail.connect()
    count = mail.select_inbox()
    print("connected!")
    print(f"Number of messages in inbox: {count}")

    messages = mail.fetch_latest(10)

    for raw_email in messages:
        msg = parse_message(raw_email)
        print("-----------------")
        print("from:", msg.get("from"))
        print("subject:", msg.get("subject"))
        print("date:", msg.get("date"))
        print("body:", msg.get("body"))
finally:
    mail.disconnect()
