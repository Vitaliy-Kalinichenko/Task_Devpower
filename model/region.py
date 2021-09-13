from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base


class Region(Base):
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    # countries = relationship('Country', back_populates='region')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Region [ID: {self.id}, Name: {self.name}, countries: {self.countries}'
