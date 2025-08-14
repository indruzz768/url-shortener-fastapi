import random, string
from sqlalchemy.orm import Session
from . import models, schemas

ALPHABET = string.ascii_letters + string.digits

def _random_code(length: int = 6) -> str:
    return ''.join(random.choices(ALPHABET, k=length))

def generate_unique_code(db: Session, length: int = 6) -> str:
    attempts = 0
    code = _random_code(length)
    while db.query(models.URL).filter_by(short_code=code).first():
        attempts += 1
        if attempts >= 5:
            length += 1
            attempts = 0
        code = _random_code(length)
    return code

def create_short_url(db: Session, payload: schemas.URLCreate) -> models.URL:
    code = generate_unique_code(db)
    obj = models.URL(original_url=str(payload.original_url), short_code=code)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_by_code(db: Session, code: str):
    return db.query(models.URL).filter_by(short_code=code).first()

def list_recent(db: Session, limit: int = 100):
    return db.query(models.URL).order_by(models.URL.created_at.desc()).limit(limit).all()

def increment_click(db: Session, obj: models.URL):
    obj.clicks = (obj.clicks or 0) + 1
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
