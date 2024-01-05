from sqlalchemy import create_engine
from sqlalchemy import (Column,Integer,String,ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()
engine  =  create_engine('sqlite:///freebies.db')

class Company:
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year =Column(Integer())

# represent data
    def __repr__(self):
        return  f"company: {self.id}"\
        f"name: {self.name}"\
        f"founding year : {self.founding_year}"
    

# establish relationship to freeble
    freebie = relationship('Freebie', backref= 'company')

class Dev:
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

# represent data
    def __repr__(self):
        return f"dev {self.id}:"\
        f"name:{self.name}"\
        


# establish relationship to freeble
    dev =  relationship('Freebie', backref = 'dev')

class Freebie:
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())

# represent data
    def __repr__(self):
        return f"freebie {self.id}:"\
        f"item name:{self.item_name}"\
        f"value:{self.value}"


# establish connection to both company and dev
    company_id = Column(Integer(), ForeignKey('company_id'))
    dev_id = Column(Integer(), ForeignKey('dev_id'))