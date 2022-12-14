import email
from db.database import Base
from sqlalchemy import Column, Integer, String


class Dbuser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)