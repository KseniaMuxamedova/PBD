import whooshalchemy as whooshalchemy

from app_config import db
from flask_sqlalchemy import SQLAlchemy

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc


class Collection(db.Model):
    __tablename__ = 'collection'
    id = db.Column('id', db.INTEGER, primary_key=True, nullable=False)
    year = db.Column('year', db.INTEGER, nullable=False)
    designer = db.Column('designer', db.String(45), nullable=False)
    model_ID = db.Column('model_ID', db.String, primary_key=True, nullable=False)
    model_company_INN = db.Column('model_company_INN', db.INTEGER, primary_key=True, nullable=False)
    journal_ID = db.Column('journal_ID', db.INT, primary_key=True, nullable=False)

class Company(db.Model):
    __tablename__ = 'company'
    inn = db.Column('INN', db.INTEGER, primary_key=True, nullable=False, unique=True)
    name = db.Column('name', db.TEXT(45), nullable=False)
    companycol = db.Column('companycol', db.TEXT)

class Models(db.Model):
    __tablename__ = 'model'
    id = db.Column('id', db.INTEGER, primary_key=True, nullable=False)
    pattern = db.Column('pattern', db.TEXT(45), nullable=False)
    sizes = db.Column('sizes', db.String(45), nullable=False)
    algoritnm = db.Column('algoritnm', db.TEXT, nullable=False)
    result = db.Column('result', db.TEXT, nullable=False)
    fabric_consumption = db.Column('fabric_consumption', db.INT, nullable=False)
    company_INN = db.Column('company_INN', db.INTEGER, nullable=False)

class Journal(db.Model):
    __tablename__ = 'journal'
    id = db.Column('ID', db.INTEGER, primary_key=True, nullable=False)
    name = db.Column('name', db.TEXT(45))
    date_of_issue = db.Column('date_of_issue', db.DATE)





