from sqlalchemy.orm import Session

from src.models import models, schemas


def get_template_by_event(db: Session, event: str):
    return db.query(models.Template).filter(models.Template.event == event).first()


def create_template(db: Session, template: schemas.TemplateIn):
    db_template = models.Template(event=template.event, title=template.title, text=template.text)
    db.add(db_template)
    db.commit()
    db.refresh(db_template)
    return db_template


def change_template(db: Session, template: schemas.TemplateIn, db_template: schemas.TemplateSchema):
    db_template.title = template.title
    db_template.text = template.text
    db.add(db_template)
    db.commit()
    db.refresh(db_template)
    return db_template
