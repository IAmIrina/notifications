from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.postgres import get_db
from src.models import schemas
from src.services import crud

router = APIRouter()


@router.post("/", response_model=schemas.TemplateSchema)
def create_template(template: schemas.TemplateIn, db: Session = Depends(get_db)):
    db_template = crud.get_template_by_event(db, event=template.event)
    if db_template:
        raise HTTPException(status_code=400, detail="Template already registered")
    return crud.create_template(db=db, template=template)


@router.put("/{event}", response_model=schemas.TemplateSchema)
def change_template(event: str, template: schemas.TemplateIn, db: Session = Depends(get_db)):
    db_template = crud.get_template_by_event(db, event=event)
    if not db_template:
        raise HTTPException(status_code=404, detail="Event not found")
    return crud.change_template(db=db, template=template, db_template=db_template)
