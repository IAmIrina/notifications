from uuid import UUID

from pydantic import BaseModel


class TemplateIn(BaseModel):
    event: str
    instant_event: bool
    title: str
    text: str


class TemplateSchema(TemplateIn):
    id: int

    class Config:
        orm_mode = True


class Event(BaseModel):
    users: list[UUID]
    event: str
    data: dict


class Notification(Event):
    template: str
    subject: str
