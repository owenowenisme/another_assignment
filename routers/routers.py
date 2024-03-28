from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from schema.users import User, UserCreate, UserUpdate, UserResponse
from model import model
from curd import crud
from db.db import get_db

router = APIRouter()

@router.get("/user")
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        res = crud.get_user(db,user_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail={"message": "Database error", "error": str(e)})
    except Exception as e:
        raise HTTPException(status_code=500,detail={"message": "Unable to fetch user", "error": e})
    if res is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": res}

@router.post("/user")
def create_user(user: UserCreate,db: Session = Depends(get_db)):
    try:
        res = crud.create_user(db,user)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail={"message": "User not created", "error": "Email already exists"})
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail={"message": "Database error", "error": str(e)})
    except Exception as e:
        raise HTTPException(status_code=500, detail={"message": "User not created", "error": str(e)})
    if res is None:
        raise HTTPException(status_code=404, detail={"message": "User not created"})
    return {"status":"User created successfully","message": res}

@router.put("/user")
def update_user(user: UserUpdate,db: Session = Depends(get_db)):
    try :
        res=crud.update_user(db,user)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail={"message": "Database error", "error": str(e)})
    except Exception as e:
        raise HTTPException(status_code=500, detail={"message": "User not updated", "error": str(e)})
    if res is None:
        raise HTTPException(status_code=404, detail="User not exists")
    
    return {"status":"User updated successfully","message": res}

@router.delete("/user")
def delete_user(user_id: int,db: Session = Depends(get_db)):
    try:
        res = crud.delete_user(db,user_id)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail={"message": "Database error", "error": str(e)})
    except Exception as e:
        raise HTTPException(status_code=500, detail={"message": "User not deleted", "error": str(e)})
    if res is None:
        raise HTTPException(status_code=404, detail="User not exists")

    return {"status":"User deleted successfully","deleted_user": res}
