import smtplib
import ssl

smtp_host = "smtp.mail.me.com"
smtp_port = 587

class ICloudMail:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def send(self, message):
        context = ssl.create_default_context()

        with smtplib.SMTP(
            smtp_host,
            smtp_port,
            timeout=20,
        ) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(self.email, self.password)
            server.send_message(message)