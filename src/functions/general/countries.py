from sqlalchemy.orm import Session
from src.models.countries import Country
from src.api.general.countries import getCountries
from types import SimpleNamespace
from src.database.db import SessionLocal

def createCountry(db: Session, name: str, code: str, flag: str):
    new = Country(name=name, code=code, flag=flag)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def getCoutry(db: Session, Country_id: int):
    return db.query(Country).filter(Country.id == Country_id).first()

def getAllCountries(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Country).offset(skip).limit(limit).all()

def updateCountry(db: Session, country_id: int, country_name: str = None, country_code: str = None, country_flag: str = None):
    Country = db.query(Country).filter(Country.id == country_id).first()
    if Country:
        if country_name:
            Country.name = country_name
            Country.code = country_code
            Country.flag = country_flag
        db.commit()
        db.refresh(Country)
    return Country

def createCountries():
    countries_return = getCountries()
    
    obj = SimpleNamespace(**countries_return)

    if(obj.errors == []):
        countries = obj.response
        db = SessionLocal()
        for ct in countries:
            ctObj = SimpleNamespace(**ct)

            createCountry(db, ctObj.name, ctObj.code, ctObj.flag)      
    