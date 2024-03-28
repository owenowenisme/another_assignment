from sqlalchemy.orm import Session
from model import model
from schema import users
from hashlib import sha256

def get_user(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()

def create_user(db: Session, user: users.UserCreate):
    password_hash = sha256(user.password.encode()).hexdigest()
    db_user = model.User(name=user.name, email=user.email, password_hash=password_hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: users.UserUpdate):
    if user.password is None and user.name is None and user.email is None:
        raise Exception("Please fill in at least one field")
    
    db_user = db.query(model.User).filter(model.User.id == user.id).first()
    if db_user is None:
        return None
    if user.name:
        db_user.name = user.name
    if user.email:
        db_user.email = user.email
    if user.password:
        password_hash = sha256(user.password.encode()).hexdigest()
        db_user.password_hash = password_hash

    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(model.User).filter(model.User.id == user_id).first()
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
