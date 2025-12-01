from apscheduler.schedulers.background import BackgroundScheduler
from .database import get_session
from .email_ingestor import ingest_emails

def start_scheduler():
    scheduler = BackgroundScheduler()

    def run_ingest():
        from sqlmodel import Session
        from .database import engine
        with Session(engine) as session:
            ingest_emails(session)

    scheduler.add_job(run_ingest, "interval", minutes=10)
    scheduler.start()
