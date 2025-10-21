from venv import create
from sqlalchemy.orm import Session
from app.models.url import URL
from app.schema.url import URLBase
import string
import random

def create_random_short_code(length:int = 6) -> str:
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def create_db_url(db: Session, url: URLBase) -> URL:
    short_code = create_random_short_code()
    db_url = URL(target_url=url.target_url, short_code=short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_db_url_by_code(db: Session, short_code: str) -> URL:
    return db.query(URL).filter(URL.short_code == short_code).first()

