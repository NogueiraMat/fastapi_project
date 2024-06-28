from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import models
from database.database import SessionLocal, engine
import database.crud as crud
from .schemas import CreateCrew, ResponseCreateCrew

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def connection():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.post("/crew", response_model=ResponseCreateCrew)
def create_crew(crew: CreateCrew, db: Session = Depends(connection)):
    new_crew = crud.create_crew(
        name=crew.name, 
        ship=crew.ship,
        db=db
    )

    return new_crew

@router.post("/character")
def create_character(name, bounty, nickname, primary_color, secondary_color, crew_id, db: Session = Depends(connection)):
    char = crud.create_character(
        name=name,
        bounty=bounty,
        nickname=nickname,
        primary_color=primary_color,
        secondary_color=secondary_color,
        crew_id=crew_id,
        db=db
    )

    return {
        "message": "Crew created successfully!",
        "crew": char
    }

@router.get("/crew")
def view_crews(db: Session = Depends(connection)):
    crews = crud.view_crews(db=db)

    return crews

@router.get("/character")
def view_characters(db: Session = Depends(connection)):
    chars = crud.view_characters(db=db)

    return {
        "message": "Crews fetched successfully!",
        "data": chars
    }


@router.get("/")
def server_root():
    return {
        "message": "server on..."
    }
