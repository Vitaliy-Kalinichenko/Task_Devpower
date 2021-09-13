from app.parse import parse
from model.country import Country
from database.database import create_db, Session


def create_database():
    create_db()
    load_data(Session())


def load_data(session):
    data = parse()
    for item in data:
        country = Country(item[0], item[1], int(item[2]))
        session.add(country)
    session.commit()
    session.close()


if __name__ == '__main__':
    create_database()
