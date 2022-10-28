from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.postgres import get_db
from models import schemas
from services import crud

router = APIRouter()


@router.post("/", response_model=schemas.TemplateSchema, summary="Create a template")
def create_template(template: schemas.TemplateIn, db: Session = Depends(get_db)):
    """
    Create a template for the event:

    - **event**: event to notification
    - **instant_event**: instant notification or not
    - **title**: subject for notification
    - **text**: template for notification
    """
    db_template = crud.get_template_by_event(db, event=template.event)
    if db_template:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Template already registered")
    return crud.create_template(db=db, template=template)


@router.put("/{event}", response_model=schemas.TemplateSchema, summary="Change a template")
def change_template(event: str, template: schemas.TemplateIn, db: Session = Depends(get_db)):
    """
    Change a template for the event:

    - **event**: event to notification
    - **instant_event**: instant notification or not
    - **title**: subject for notification
    - **text**: template for notification
    """
    db_template = crud.get_template_by_event(db, event=event)
    if not db_template:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Event not found")
    return crud.change_template(db=db, template=template, db_template=db_template)
