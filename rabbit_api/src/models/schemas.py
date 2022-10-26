from uuid import UUID

from pydantic import BaseModel


class TemplateIn(BaseModel):
    event: str
    title: str
    text: str


class TemplateSchema(BaseModel):
    id: int
    event: str
    title: str
    text: str

    class Config:
        orm_mode = True


class Event(BaseModel):
    users: list[UUID]
    event: str
    data: dict


class Notification(Event):
    template: str
    subject: str
