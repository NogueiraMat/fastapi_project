from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from database import models
from database.models import Crew
from database.database import SessionLocal
from fastapi import HTTPException, status
from api.schemas import ResponseCreateCrew

def create_character(db: Session, name: str, bounty: int, nickname: str, primary_color: str, secondary_color: str, crew_id: int):
    try:
        crew = db.query(Crew).filter_by(id=crew_id).one()
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Crew '{crew_id}' does not exist. Please create the crew first.")
    
    new_character = models.Characters(
        name=name,
        bounty=bounty,
        nickname=nickname,
        primary_color=primary_color,
        secondary_color=secondary_color,
        crew_id=crew_id
    )

    db.add(new_character)
    db.commit()
    db.refresh(new_character)

    return new_character.name

def create_crew(db: Session, name: str, ship: str) -> ResponseCreateCrew:
    new_crew = models.Crew(
        name=name,
        ship=ship
    )

    db.add(new_crew)
    db.commit()
    db.refresh(new_crew)

    return ResponseCreateCrew(message="Crew created successfully!", crew=new_crew.name)

def view_characters(db: Session):
    chars = db.query(models.Characters).all()

    return chars

def view_crews(db: Session):
    crews = db.query(models.Crew).all()
    
    return {
        "message": "Crews fetched successfully!",
        "data": crews
    }