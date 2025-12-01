import imaplib
import email
from email.header import decode_header
from datetime import datetime
from sqlmodel import Session
from .models import Email
from .region_classifier import classify_region

IMAP_SERVER = "imap.zoho.in"
EMAIL_USER = "sheshagirikulkarni@zohomail.in"
APP_PASSWORD = "gKzP K9mp cSrB"

def clean_header(value):
    if value is None:
        return ""
    decoded, charset = decode_header(value)[0]
    if charset:
        return decoded.decode(charset)
    return decoded if isinstance(decoded, str) else decoded.decode()

def ingest_emails(session: Session):
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_USER, APP_PASSWORD)

    mail.select("INBOX")

    status, msg_ids = mail.search(None, "ALL")
    msg_list = msg_ids[0].split()

    for msg_id in msg_list:
        status, data = mail.fetch(msg_id, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])

        subject = clean_header(msg["subject"])
        sender = clean_header(msg["from"])
        date = msg["date"]

        # Extract body
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode(errors="ignore")
                    break
        else:
            body = msg.get_payload(decode=True).decode(errors="ignore")

        region = classify_region(sender, subject)

        email_obj = Email(
            subject=subject,
            sender=sender,
            received_at=date,
            region=region,
            body=body
        )
        session.add(email_obj)

    session.commit()
    mail.logout()

    return {"status": "Emails ingested"}
