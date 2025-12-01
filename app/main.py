from fastapi import FastAPI, Depends, Request
from sqlmodel import Session, select
from .database import create_db, get_session
from .models import Email
from .email_ingestor import ingest_emails
from .scheduler import start_scheduler

# -------------------------------
# OWASP SECURITY HEADERS (UPDATED)
# -------------------------------
from secure import Secure

secure_headers = Secure()  # NEW API (SecureHeaders is deprecated)

# -------------------------------
# FASTAPI APP INIT
# -------------------------------
app = FastAPI()

# Apply OWASP Security Headers
@app.middleware("http")
async def set_secure_headers(request: Request, call_next):
    response = await call_next(request)
    secure_headers.framework.fastapi(response)  # correct function
    return response

# -------------------------------
# STARTUP EVENTS
# -------------------------------
@app.on_event("startup")
def startup():
    create_db()
    start_scheduler()

# -------------------------------
# ROUTES
# -------------------------------
@app.get("/ingest")
def ingest(session: Session = Depends(get_session)):
    return ingest_emails(session)

@app.get("/emails")
def get_emails(region: str, session: Session = Depends(get_session)):
    emails = session.exec(select(Email).where(Email.region == region)).all()
    return emails
