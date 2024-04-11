# https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/ flask SQLAlchemy docs
# Note: Whoever works on this will need to run "pip install -U Flask-SQLAlchemy" into this directory
# Use comments please and thank youuuu

from flask_sqlalchemy import SQLAlchemy as sql
from sqlalchemy import MetaData, create_engine, Table, text, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#import app
#import os

#import
#db = sql(app)
engine = create_engine("mysql+pymysql://reagent_app:password@localhost/reagentLabelDB")

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://reagent_app:password@localhost/reagentLabelDB' # fill in with correct url
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #keeps it from complaining in the console

metadata = MetaData()
Base = declarative_base()
    
Reagent = Table('label',
                metadata,
                Column('upc', Integer, primary_key=True),
                Column('initials', String(5)),
                Column('lot', Integer),
                Column('reagent', String(50)),
                Column('openedDate', DateTime),
                Column('expirationDate', DateTime)
                )

reagentExpiration = Table('reagentExpiration',
                metadata,
                Column('expiration', Integer),
                Column('reagent', String(50), ForeignKey('label.reagent'), primary_key=True)
                )

metadata.create_all(engine)

#establish connection from engine
with engine.connect() as connection:
    #inserting db with mysql script

    result = connection.execute(Reagent.select())
    for row in result:
        print(row)
    result.close()