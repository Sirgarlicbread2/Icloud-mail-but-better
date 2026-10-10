import imaplib

IMAP_HOST = "imap.mail.me.com"
IMAP_PORT = 993


class ICloudMailIMAP:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.connection = None

    def connect(self):
        self.connection = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
        self.connection.login(self.email, self.password)

    def select_inbox(self):
        status, data = self.connection.select("INBOX")

        if status != "OK":
            raise RuntimeError("Inbox could not be opened.")
        return int(data[0])

    def disconnect(self):
        if self.connection:
            self.connection.logout()
            self.connection = None

    def fetch_latest(self, count=10):
        status, data = self.connection.search(None, "ALL")

        if status != "OK":
            raise RuntimeError("Failed to fetch latest emails.")

        message_ids = data[0].split()
        latest_ids = message_ids[-count:]
        messages = []

        for message_id in reversed(latest_ids):
            status, data = self.connection.fetch(message_id, "(RFC822)")

            if status != "OK":
                continue

            raw_email = data[0][1]
            messages.append(raw_email)

        return messages
