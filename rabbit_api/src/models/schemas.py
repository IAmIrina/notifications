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
