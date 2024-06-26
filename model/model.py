from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from db.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)

    class Config:
        orm_mode = True
