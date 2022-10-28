from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.postgres import get_db
from models import schemas
from services import crud

router = APIRouter()


@router.post("/", response_model=schemas.TemplateSchema)
def create_template(template: schemas.TemplateIn, db: Session = Depends(get_db)):
    db_template = crud.get_template_by_event(db, event=template.event)
    if db_template:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Template already registered")
    return crud.create_template(db=db, template=template)


@router.put("/{event}", response_model=schemas.TemplateSchema)
def change_template(event: str, template: schemas.TemplateIn, db: Session = Depends(get_db)):
    db_template = crud.get_template_by_event(db, event=event)
    if not db_template:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Event not found")
    return crud.change_template(db=db, template=template, db_template=db_template)
