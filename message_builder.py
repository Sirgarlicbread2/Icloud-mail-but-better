from email.message import EmailMessage

def create_message(
        sender,
        to,
        subject,
        text,
        cc=None,
        bcc=None
):
    msg = EmailMessage()

    msg["From"] = sender
    msg["to"] = ", ".join(to)
    msg["subject"] = subject

    if cc:
        msg["Cc"] = ", ".join(cc)
    if bcc:
        msg["Bcc"] = ", ".join(bcc)

    msg.set_content(text)

    return msg