# import imaplib

# EMAIL = "sheshagirikulkarni@zohomail.in"
# APP_PASSWORD = "2piX LgwK M4aL"

# try:
#     mail = imaplib.IMAP4_SSL("imap.zoho.com", 993)
#     mail.login(EMAIL, APP_PASSWORD)
#     print("LOGIN SUCCESS")
# except Exception as e:
#     print("LOGIN FAILED:", e)
    
    
    
import imaplib
import ssl

EMAIL = "sheshagirikulkarni@zohomail.in"
APP_PASSWORD = "2piXLgwKM4aL"

try:
    # Create SSL context
    context = ssl.create_default_context()
    
    # Connect to Zoho IMAP
    mail = imaplib.IMAP4_SSL("imap.zoho.in", 993, ssl_context=context)
    
    # Enable debug mode to see detailed errors
    mail.debug = 4
    
    # Attempt login
    mail.login(EMAIL, APP_PASSWORD)
    print("✓ LOGIN SUCCESS")
    
    # List mailboxes to confirm
    status, mailboxes = mail.list()
    print(f"✓ Found {len(mailboxes)} mailboxes")
    
    mail.logout()
    
except imaplib.IMAP4.error as e:
    print(f"✗ IMAP ERROR: {e}")
except Exception as e:
    print(f"✗ LOGIN FAILED: {e}")
