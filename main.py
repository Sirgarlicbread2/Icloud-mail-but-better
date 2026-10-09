from smtp_client import ICloudMail
from message_builder import create_message

EMAIL = input("enter your email:")
PASSWORD = input("enter your password"
)
message = create_message(
    sender=EMAIL,
    to=[
        #redacted
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