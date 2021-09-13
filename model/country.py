from sqlalchemy import Column, Integer, String
from database.database import Base


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    region = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)

    def __init__(self, name, region, population):
        self.name = name
        self.region = region
        self.population = population

    def __repr__(self):
        return f'Country: {self.name}, region: {self.region}, population: {self.population}'
