from sqlalchemy.orm import Session
from src.models.timezones import Timezone
from src.api.general.timezone import getTimezones
from types import SimpleNamespace
from src.database.db import SessionLocal

def createTimezone(db: Session, timezone: str):
    new_timezone = Timezone(timezone=timezone)
    db.add(new_timezone)
    db.commit()
    db.refresh(new_timezone)
    return new_timezone

def getTimezone(db: Session, Timezone_id: int):
    return db.query(Timezone).filter(Timezone.id == Timezone_id).first()

def getTimezone(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Timezone).offset(skip).limit(limit).all()

def updateTimezone(db: Session, timezone_id: int, timezone_name: str = None):
    Timezone = db.query(Timezone).filter(Timezone.id == timezone_id).first()
    if Timezone:
        if timezone_name:
            Timezone.timezone = timezone_name
        db.commit()
        db.refresh(Timezone)
    return Timezone

def deleteTimezone(db: Session, timezone_id: int):
    Timezone = db.query(Timezone).filter(Timezone.id == timezone_id).first()
    if Timezone:
        db.delete(Timezone)
        db.commit()
    return Timezone

def createTimezones():
    timezones_return = getTimezones()
    
    obj = SimpleNamespace(**timezones_return)

    if(obj.errors == []):
        timezones = obj.response
        db = SessionLocal()
        for tz in timezones:
            createTimezone(db, tz)      
    