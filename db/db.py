from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
SQLALCHEMY_DATABASE_URL = "sqlite:///example.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

Session = sessionmaker(autocommit=False, autoflush=False,bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
