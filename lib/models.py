from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///freebies.db')
Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    # establish relationship to freebie
    freebie = relationship('Freebie', backref='company')

    # represent data
    def __repr__(self):
        return f"company: {self.id}, " \
               f"name: {self.name}, " \
               f"founding year: {self.founding_year}"

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    # establish relationship to freebie
    freebie = relationship('Freebie', backref='dev')

    # represent data
    def __repr__(self):
        return f"dev {self.id}: " \
               f"name: {self.name}"

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())

    # establish connection to both company and dev
    company_id = Column(Integer(), ForeignKey('companies.id'))
    dev_id = Column(Integer(), ForeignKey('devs.id'))

    # represent data
    def __repr__(self):
        return f"freebie {self.id}: " \
               f"item name: {self.item_name}, " \
               f"value: {self.value}"

Base.metadata.create_all(engine)