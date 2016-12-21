from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///database_files/amity.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class PersonModel(Base):
    __tablename__ = 'people'
    person_id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    designation = Column(String(255))
    office = Column(Integer(), ForeignKey('rooms.room_id'))
    living_space = Column(Integer(), ForeignKey('rooms.room_id'))


class RoomModel(Base):
    __tablename__ = 'rooms'
    room_id = Column(Integer(), primary_key=True)
    room_name = Column(String(255))
    room_type = Column(String(255))
    room_capacity = Column(Integer())


Base.metadata.create_all(engine)
