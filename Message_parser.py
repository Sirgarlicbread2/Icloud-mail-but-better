from email import policy
from email.parser import BytesParser

def parse_message(raw_email):
    msg = BytesParser(
        policy=policy.default
    ).parsebytes(raw_email)
    body = msg.get_body(
preferencelist=("plain", "html")
    )

    if body:
        content = body.get_content()
    else:
        content = None

    
    return{
        "from": msg.get("From"),
        "to": msg.get("To"),
        "subject": msg.get("Subject"),
        "date": msg.get("Date"),
        "message_id": msg.get("Message-ID"),
        "body": content,
    }
