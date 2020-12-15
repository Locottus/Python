from sqlalchemy import create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

db_string = "postgres://postgres:Guatemala1@localhost/test"

db = create_engine(db_string)  
base = declarative_base()

'''
class Film(base):  
    __tablename__ = 'filmen'

    title = Column(String, primary_key=True)
    director = Column(String)
    year = Column(String)
'''
    

class Clients(base):  
    __tablename__ = 'Clients'
    client_id = Column(String, primary_key=True)
    client = Column(String)


class Allergies(base):  
    __tablename__ = 'Allergies'
    id = Column(String, primary_key=True)
    total = Column(String )
    per_page  = Column(String )
    current_page  = Column(String )
    last_page  = Column(String )
    next_page_url  = Column(String )
    prev_page_url  = Column(String )
    From = Column(String )
    to = Column(String )
    allergy_pk = Column(String)
    client_id = Column(String)
    patient_id = Column(String)
    allergy_id = Column(String)
    enc_id = Column(String)
    Type = Column(String)
    description = Column(String)
    onset_date = Column(String)
    resolved_date = Column(String)
    severity = Column(String)
    reaction_code= Column(String)
    reaction= Column(String)
    product_code= Column(String)
    comment= Column(String)
    hj_create_timestamp = Column(String)
    hj_modify_timestamp = Column(String)
    


                      
    

Session = sessionmaker(db)  
session = Session()

base.metadata.create_all(db)

# Create 
'''
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
