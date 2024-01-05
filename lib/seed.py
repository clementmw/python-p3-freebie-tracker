from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Base, engine, Company, Dev, Freebie

Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

# # to delete
# session.query(Company).delete()
# session.query(Dev).delete()
# session.query(Freebie).delete()

companies = [
    Company(name=fake.company(), founding_year=fake.year())
    for _ in range(5)
]
session.add_all(companies)

devs = [
    Dev(name=fake.name())
    for _ in range(5)
]
session.add_all(devs)

freebies = [
    Freebie(
        item_name=fake.word(),
        value=fake.pyint(),
        company=fake.random_element(companies),
        dev=fake.random_element(devs)
    )
    for _ in range(5)
]
session.add_all(freebies)

session.commit()
