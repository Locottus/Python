from sqlalchemy import create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker


db_string = "postgres://postgres:Guatemala1@localhost:5432/healthjump"

db = create_engine(db_string)  
base = declarative_base()

class Client(base):  
    __tablename__ = 'clients'
    client = Column(String, primary_key=True)
    

Session = sessionmaker(db)  
session = Session()

base.metadata.create_all(db)


'''

# Create 
doctor_strange = Film(title="Doctor Strange", director="Scott Derrickson", year="2016")  
session.add(doctor_strange)  
session.commit()

# Read
films = session.query(Film)  
for film in films:  
    print(film.title)

# Update
doctor_strange.title = "Some2016Film"  
session.commit()

# Delete
session.delete(doctor_strange)  
session.commit()  
'''
